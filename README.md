# sipa

### Instalación

Sipa corre en python 2.7.x (no probado con 3.x), requiere de npyscreen, el cual se puede instalar mendiante pip, además requiere RPi.GPIO para el manejo del puerto serial.

    $ sudo pip install npyscreen RPi.GPIO

Descarga el programa 

    $ git clone https://github.com/luisza/sipa.git 
    $ cd sipa
    
Puede utilizar pip -r requierement.txt para instalar las dependencias necesarias si todavía no las ha instalado.

### Ejecución 

Sipa está pensado para correrse en un rasberry pi, y utiliza los pines GIO, por lo que se requiere permisos de super usuario.

    $ sudo python2 main.py


