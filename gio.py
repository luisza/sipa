
import logging
"""
logger.basicConfig(filename='GIO.log', filemode='w',
                    level=logger.DEBUG, 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p')
"""



logger = logging.getLogger('_GIO_')
fh = logging.FileHandler('logs/GIO.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class GIO:
    BCM = 'BCM'
    IN = 'IN'
    OUT = 'OUT'
              # entrada de agua
    inputs = [False, False, False, False, # 0
              False, False, False, True,  # 1
              False, False, True, False,  # 2
              False, False, True, True,   # 3
              False, True, False, False, # 4
              False, True, False, False, # 4 
              # salida de agua
              False, False, True, True,   # 3
              False, False, True, False,  # 2
              False, False, False, True,  # 1
              False, False, False, False, # 0

             ]  
    in_pos = 0    




    def setup(self, pin, pin_type):
        logger.debug('Setup %d is %s'%( pin, str(pin_type) ) )
    
    def cleanup(self):
        logger.debug('Cleanup')     

    def setmode(self, mode):
        logger.debug('set mode %s'%(mode,))                          
              
    
    def input(self, pin):
        value = self.inputs[self.in_pos]
        logger.debug('Input %d is %s in %s'%(self.in_pos, 
                                              str(value),
                                              str(pin)                
                                              )) 
        self.in_pos = (self.in_pos+1) % (len(self.inputs))
  
        return value


    def output(self, pin, state):
        logger.debug('Output pin %d is %s'%(pin, str(state) ))  
 
