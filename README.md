# Esteganografía con imágenes en LSB con RenPy

* Codigo basado en el trabajo de [parzibyte](https://github.com/parzibyte/esteganografia-python)
* Una explicacion sencilla se encuentra en el siguiente [blog](https://parzibyte.me/blog/2018/04/05/esteganografia-imagenes-lsb/)

~~~~
show oveja at topleft
$ mensaje=renpy.input("Insert you message here")
$ a=esteganografia_escribir(mensaje,"images/oveja.png","images/output.png")
e "Guardaste el mensaje en el siguiente archivo."
show expression "images/output.png" at topright
$ mensaje_foto=esteganografia_leer("output.png").leer_texto()
e "El mensaje es el siguiente:"
e "[mensaje_foto]"
~~~~

asdaasdasd
