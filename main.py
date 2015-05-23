#!/usr/bin/env python
# encoding: utf-8

import npyscreen, curses
import threading

from forms import motorForm, ValvulasForm, SensorForm, ConfMotor, ConfSensor
from constants import GIO, Mconfig, MOTOR_MOVES, DISOLUCION_CLORO


class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

class MainForm(npyscreen.FormWithMenus):
    def create(self):
        self.t = 0
        self.timer = None
        self.in_menu = False
        self.conf = Mconfig()
        self.load_conf(self.conf)
        self.add(npyscreen.FixedText, name = "Text:", value= "Sistema de control %d"%(self.t) )
        self.stat = self.add(npyscreen.MultiLineEdit, name = "stat", value= "", editable=False)
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application    
        
        # The menus are created here.
        self.m1 = self.add_menu(name="Pines", shortcut="1")
        self.m1.addItemsFromList([
            ("Motor", self.motor, "m"),
            ("Valvulas", self.valvulas, "v"),
            ("Sensor", self.sensor, "s"),
        ])
        
        self.m2 = self.add_menu(name="Configuraciones", shortcut="2",)
        self.m2.addItemsFromList([
            ("Motor",   self.conf_motor),
            ("Sensor",   self.conf_sensor),
        ])
        
    
        self.m2 = self.add_menu(name="Save/Exit", shortcut="3",)
        self.m2.addItemsFromList([
            ("Save",   self.save, "^s"),
            ("---------",   curses.beep ),
            ("Exit",   self.exit_application),
        ])
        self.display_async()
        
    def load_conf(self, conf):
        conf.load()

    def save(self):
        self.conf.save()

    def motor(self):
        F = motorForm(self.conf, name='Pines del motor')
        F.edit()
        self.conf.IN1 =  F.in1.value[0] 
        self.conf.IN2 = F.in2.value[0]
        self.conf.IN3 = F.in3.value[0]
        self.conf.IN4 = F.in4.value[0]

    def valvulas(self):
        F = ValvulasForm(self.conf, name='Pines de las valvulas')
        F.edit()
        self.conf.VENTRADA =  F.ventrada.value[0], 
        self.conf.VSALIDA = F.vsalida.value[0]
        self.conf.VCLORO = F.vcloro.value[0]

    def sensor(self):
        F = SensorForm(self.conf, name='Pines del sensor')
        F.edit()
        self.conf.S1 = F.s1.value[0]
        self.conf.S2 = F.s2.value[0]
        self.conf.S3 = F.s3.value[0]


    def conf_motor(self):
        F = ConfMotor(self.conf, name='Configuraciones del motor')
        F.edit()

        self.conf.TIPO_ROTACION = F.tipo_rotacion.value[0]
        
        tr = self.conf.TIEMPO_ROTACION 
        try:
            self.conf.TIEMPO_ROTACION = int(F.tiempo_rotacion.value)
        except:
            self.conf.TIEMPO_ROTACION = tr

    def conf_sensor(self):
        F =  ConfSensor(self.conf, name='Configuraciones del sensor')
        F.edit()      
        self.conf.DISOLUCION_CLORO = F.dis_cloro.value[0]

        ll = self.conf.LLENADO
        try:
            self.conf.LLENADO = int(F.llenado.value)
        except:
            self.conf.LLENADO = ll

    def exit_application(self):
        curses.beep()
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()
        if self.timer:
            self.timer.cancel()
    


    def display(self, clear=False):
       if not clear:
           self._widgets__[0].value = "refresco %d"%(self.t)
           self.t += 1
           self.stat.value = """
    Pines                                                           Configuración y lecturas
----------------------------------------------                  ------------------------------
Motor [IN1-4]:  %(IN1)s %(IN2)s %(IN3)s %(IN4)s                      
                                                                Tiempo rotación: %(tiempo_rotacion)d s
Valvulas [ent,sal,cloro]: %(ventrada)s %(vsalida)s %(vcloro)s                  
                                                                Tipo: %(tipo_rotacion)s
Sensor [S1-3]: %(S1)s %(S2)s %(S3)s                                
                                                                Leyendo: %(lectura)s de %(llenado)d
Solución de cloro: %(cloro)s
           """%{
        'IN1': GIO[self.conf.IN1],
        'IN2': GIO[self.conf.IN2],
        'IN3': GIO[self.conf.IN3],
        'IN4': GIO[self.conf.IN4],
        'ventrada': GIO[self.conf.VENTRADA],
        'vsalida': GIO[self.conf.VSALIDA],
        'vcloro': GIO[self.conf.VCLORO],
        'S1': GIO[self.conf.S1],
        'S2': GIO[self.conf.S2],
        'S3': GIO[self.conf.S3],
        'lectura': '100',
        'tiempo_rotacion': self.conf.TIEMPO_ROTACION,
        'tipo_rotacion': MOTOR_MOVES[self.conf.TIPO_ROTACION],
        'llenado': self.conf.LLENADO,
        'cloro': DISOLUCION_CLORO[self.conf.DISOLUCION_CLORO]
                }

       super(MainForm, self).display(clear=clear)


    def display_async(self):
        if not self.in_menu:
            self.display()
        self.timer = threading.Timer(3.0, self.display_async)
        self.timer.start()

    def root_menu(self, *args):
        self.in_menu=True
        super(MainForm, self).root_menu(*args)
        self.in_menu=False
def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()

