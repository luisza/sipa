try:
    import RPi.GPIO as GPIO
except:
    from gio import GIO
    GPIO = GIO()

from time import sleep
import threading
from constants import DIS_CLORO, PIN_GPIO, GIO 

import logging
logging.basicConfig(filename='logs/DEBUG.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')



sipa_logger = logging.getLogger('sipa')
fh = logging.FileHandler('logs/sipa.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
fh.setFormatter(formatter)
sipa_logger.addHandler(fh)

class PiControl(object):
    def __init__(self, conf):
        self.conf = conf
        self.configure()
        self.thread = None
        

    def setup(self, pin, pin_type):
        GPIO.setup(PIN_GPIO[pin], pin_type)
        sipa_logger.debug('Setup %d -> PIN %s number %d in %s'%(
                           pin,
                           GIO[pin],
                           PIN_GPIO[pin],
                           str(pin_type)                                  
                      ))
        
    def configure(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

    # motor
        self.setup(self.conf.IN1, GPIO.OUT)
        self.setup(self.conf.IN2, GPIO.OUT)
        self.setup(self.conf.IN3, GPIO.OUT)
        self.setup(self.conf.IN4, GPIO.OUT)

    # Valvulas
        self.setup(self.conf.VENTRADA, GPIO.OUT)
        self.setup(self.conf.VSALIDA, GPIO.OUT)
        self.setup(self.conf.VCLORO, GPIO.OUT)

    # Sensor
        self.setup(self.conf.S1, GPIO.IN)
        self.setup(self.conf.S2, GPIO.IN)
        self.setup(self.conf.S3, GPIO.IN)
        self.setup(self.conf.S4, GPIO.IN)


    def get_sensor_value(self):
        """ Integer value in 0-8 range """
        input_sensor = [GPIO.input(self.conf.S1),
                        GPIO.input(self.conf.S2),
                        GPIO.input(self.conf.S3),
                        GPIO.input(self.conf.S4)
                       ]
        value =  int("".join(map(str, map(int, input_sensor))), 2)
        
        sipa_logger.debug( "Input sensor %s  = %d"%(repr(input_sensor), value ) )
        return value


    def water_in(self):
        GPIO.output(self.conf.VENTRADA, True)
        while self.get_sensor_value() < self.conf.LLENADO:
            sleep(1)
        GPIO.output(self.conf.VENTRADA, False)

        sipa_logger.debug("water_in out")

    def water_out(self):
        if self.thread:
            self.thread.join()
        GPIO.output(self.conf.VSALIDA, True)
        while self.get_sensor_value() > 0:
            sleep(1)
        GPIO.output(self.conf.VSALIDA, False)
            

    def cloro_in(self):
        # calculos
        volumen_cloro =  (self.conf.CONSTANTE_DE_CLORACION * self.get_volumen() 
                                ) / DIS_CLORO[self.conf.DISOLUCION_CLORO] 
        sleep_time = self.conf.TIEMPO_SALIDA_CLORO * volumen_cloro # en ml 

        sipa_logger.debug( "volumen_cloro: %s = %s * %s / %s "%(
                                    str(volumen_cloro), 
                                    str(self.conf.CONSTANTE_DE_CLORACION),  
                                    str(self.get_volumen()), 
                                    str(DIS_CLORO[self.conf.DISOLUCION_CLORO] )
                                     ) 
                      )

        sipa_logger.debug("sleep_time: %s = %s * %s" %(
                                            str(sleep_time) ,
                                            str(self.conf.TIEMPO_SALIDA_CLORO),
                                            str(volumen_cloro)
                                            )
                    )
        GPIO.output(self.conf.VCLORO, True)
        sleep(sleep_time) 
        GPIO.output(self.conf.VCLORO, False)   




    def get_volumen(self):
        return (self.conf.VOLUMEN_MAXIMO / 8)*self.get_sensor_value()


    def motor_rotate_async(self):
        pass

    def motor_rotate(self):
        self.thread = threading.Thread(target=self.motor_rotate_async, args=())
        #self.thread.daemon = True # Daemonize thread
        self.thread.start() 



    def __del__(self):
        GPIO.cleanup()

class PiManager(object):

    def __init__(self, conf):
        self.conf = conf
        self.control = PiControl(conf)
        self.running = False
        self.thread = None


    def run(self):
        self.thread = threading.Thread(target=self.run_async, args=())
        #self.thread.daemon = True # Daemonize thread
        self.thread.start() 
        return self.thread
        

    def run_async(self):
        self.running = True
        while self.running:
            sipa_logger.debug("RUN")
            self.control.water_in()
            self.control.motor_rotate()
            self.control.cloro_in()
            self.control.water_out()

    def stop(self):
        self.running = False
        

    def __del__(self):

        self.running = False
        del self.control


if __name__ == '__main__':
    from constants import Mconfig
    conf = Mconfig()
    conf.load() 
    g = PiManager(conf)
    t = g.run()
    print "Durmiendo"
    sleep(10)
    g.stop()
    t.join()
