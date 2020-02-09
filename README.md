# Esteganografía con imágenes en LSB con RenPy

Codigo basado en el trabajo de [parzibyte](https://github.com/parzibyte/esteganografia-python)
Una explicacion sencilla se encuentra en el siguiente [blog](https://parzibyte.me/blog/2018/04/05/esteganografia-imagenes-lsb/)

    # These display lines of dialogue.
    show oveja at topleft
    $ print(renpy.get_attributes("oveja"))
    $ mensaje=renpy.input("Insert you message here")
    $ a=esteganografia_escribir(mensaje,"images/oveja.png","images/output.png")
    e "Guardastes el mensaje en el siguiente archivo."
    show expression "images/output.png" at topright
    $ mensaje_foto=esteganografia_leer("output.png").leer_texto()
    e "El mensaje es el siguiente:"
    e "[mensaje_foto]"

    # This ends the game.

