# encoding: utf-8
import npyscreen
from constants import GIO, MOTOR_MOVES, DISOLUCION_CLORO

class motorForm(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(motorForm, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.in1 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='IN1', value=[self.conf.IN1,], values = GIO)
        self.in2 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='IN2', value=[self.conf.IN2,], values = GIO)
        self.in3 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='IN3', value=[self.conf.IN3,], values = GIO)
        self.in4 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='IN4', value=[self.conf.IN4,], values = GIO)


class ValvulasForm(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(ValvulasForm, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.ventrada = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Val Entrada', value=[self.conf.VENTRADA,], values = GIO)
        self.vsalida = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Val Salida', value=[self.conf.VSALIDA,], values = GIO)
        self.vcloro = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Val Cloro', value=[self.conf.VCLORO,], values = GIO)

class SensorForm(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(SensorForm, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.s1 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Entrada 1', value=[self.conf.S1,], values = GIO)
        self.s2 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Entrada 2', value=[self.conf.S2,], values = GIO)
        self.s3 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Entrada 3', value=[self.conf.S3,], values = GIO)
        self.s4 = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Entrada 4', value=[self.conf.S4,], values = GIO)


class ConfMotor(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(ConfMotor, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.tipo_rotacion  = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name='Modo de rotacion', 
                           value=[self.conf.TIPO_ROTACION,], values = MOTOR_MOVES)
        self.tiempo_rotacion = self.add(npyscreen.TitleText, name = u"Tiempo de rotación (s):", value="%d"%self.conf.TIEMPO_ROTACION)


class ConfRecipiente(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(ConfRecipiente, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.volumen = self.add(npyscreen.TitleText, name = u"Volumen máximo: ", value="%d"%self.conf.VOLUMEN_MAXIMO)
        self.llenado = self.add(npyscreen.TitleText, name = u"Porcentaje de llenado: ", value="%d"%self.conf.LLENADO)

class ConfCloro(npyscreen.Form):

    def __init__(self, conf, **kwargs):
        self.conf = conf
        super(ConfCloro, self).__init__(**kwargs)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):

        self.dis_cloro  = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=5, name=u'Porcentaje de disolución', 
                           value=[self.conf.DISOLUCION_CLORO,], values = DISOLUCION_CLORO)

        self.constante_coloracion = self.add(npyscreen.TitleText, name = u"Constante de cloración :", value="%f"%self.conf.CONSTANTE_DE_CLORACION )
        self.tiempo_salida = self.add(npyscreen.TitleText, name = u"Tiempo de salida del cloro (s x ml): ", value="%d"%self.conf.TIEMPO_SALIDA_CLORO)       

