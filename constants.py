import ConfigParser
import os

GIO = ["GPI02", "GPI03", "GPI04", "GPI017", "GPI027", "GPI022", "GPI010", 
 "GPI09", "GPI011", "GPI014", "GPI015", "GPI018", "GPI023", 
 "GPI024", "GPI025", "GPI08", "GPI07"]

DISOLUCION_CLORO = ["12 %", "15 %"]
DIS_CLORO = [12, 15]

MOTOR_MOVES = ["Clockwise", "Anti-clockwise", "Medio y Medio"]

PIN_GPIO = [ int(x.split('GPI0')[1]) for x in GIO]

class Mconfig(object):
    # Motor 
    IN1 = 2 # GPI04
    IN2 = 3 # GPI017
    IN3 = 4 # GPI027
    IN4 = 5 # GPI022

    # Valvulas
    VENTRADA = 14 # GPI025
    VSALIDA = 15  # GPI08
    VCLORO = 16   # GPI07

    # Sensor

    S1 = 6 # GPI010
    S2 = 7 # GPI09
    S3 = 8 # GPI011
    S4 = 11 # GPI018

            #[clockwise, anti-clockwise, medio y medio]
    TIPO_ROTACION = 0
    TIEMPO_ROTACION = 10

    LLENADO = 4
    DISOLUCION_CLORO = 0
    CONSTANTE_DE_CLORACION = 0.001  
    VOLUMEN_MAXIMO = 100 # ml

    TIEMPO_SALIDA_CLORO = 2  # 2 s x ml

    def save(self):
        config = ConfigParser.RawConfigParser()

        config.add_section('Pines')
        config.set('Pines', 'IN1', '%d'%self.IN1)
        config.set('Pines', 'IN2', '%d'%self.IN2)
        config.set('Pines', 'IN3', '%d'%self.IN3)
        config.set('Pines', 'IN4', '%d'%self.IN4)

        config.set('Pines', 'VENTRADA', '%d'%self.VENTRADA)
        config.set('Pines', 'VSALIDA', '%d'%self.VSALIDA)
        config.set('Pines', 'VCLORO', '%d'%self.VCLORO)


        config.set('Pines', 'S1', '%d'%self.S1)
        config.set('Pines', 'S2', '%d'%self.S2)
        config.set('Pines', 'S3', '%d'%self.S3)
        config.set('Pines', 'S4', '%d'%self.S4)

        config.add_section('Configuraciones')
        config.set('Configuraciones', 'TIPO_ROTACION', '%d'%self.TIPO_ROTACION)
        config.set('Configuraciones', 'TIEMPO_ROTACION', '%d'%self.TIEMPO_ROTACION)
        config.set('Configuraciones', 'LLENADO', '%d'%self.LLENADO)

        config.set('Configuraciones', 'DISOLUCION_CLORO', '%d'%self.DISOLUCION_CLORO)
        config.set('Configuraciones', 'CONSTANTE_DE_CLORACION', '%f'%self.CONSTANTE_DE_CLORACION)
        config.set('Configuraciones', 'VOLUMEN_MAXIMO', '%d'%self.VOLUMEN_MAXIMO)
        config.set('Configuraciones', 'TIEMPO_SALIDA_CLORO', '%d'%self.TIEMPO_SALIDA_CLORO )


        with open('config.cfg', 'wb') as configfile:
            config.write(configfile)

    def load(self):
    
        if os.path.exists('config.cfg'):
            config = ConfigParser.ConfigParser()
            config.read('config.cfg')

            self.IN1 = int(config.get('Pines', 'IN1', self.IN1))
            self.IN2 = int(config.get('Pines', 'IN2', self.IN2))
            self.IN3 = int(config.get('Pines', 'IN3', self.IN3))
            self.IN4 = int(config.get('Pines', 'IN4', self.IN4))

            self.VENTRADA = int(config.get('Pines', 'VENTRADA', self.VENTRADA))
            self.VSALIDA = int(config.get('Pines', 'VSALIDA', self.VSALIDA))
            self.VCLORO = int(config.get('Pines', 'VCLORO', self.VCLORO))

            self.S1 = int(config.get('Pines', 'S1', self.S1))
            self.S2 = int(config.get('Pines', 'S2', self.S2))
            self.S3 = int(config.get('Pines', 'S3', self.S3))
            self.S4 = int(config.get('Pines', 'S4', self.S4))

            self.TIPO_ROTACION = int(config.get('Configuraciones', 'TIPO_ROTACION', self.TIPO_ROTACION))
            self.TIEMPO_ROTACION = int(config.get('Configuraciones', 'TIEMPO_ROTACION', self.TIEMPO_ROTACION))
            self.LLENADO = int(config.get('Configuraciones', 'LLENADO', self.LLENADO))
            self.DISOLUCION_CLORO = int(config.get('Configuraciones', 'DISOLUCION_CLORO', self.DISOLUCION_CLORO))

            self.CONSTANTE_DE_CLORACION = float(config.get('Configuraciones', 'CONSTANTE_DE_CLORACION'))
            self.VOLUMEN_MAXIMO = int(config.get('Configuraciones', 'VOLUMEN_MAXIMO'))
            self.TIEMPO_SALIDA_CLORO = int(config.get('Configuraciones', 'TIEMPO_SALIDA_CLORO' ) )



