# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image black = "#000000"
image oveja = "images/oveja.png"

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen

    # These display lines of dialogue.
    show oveja at topleft
    $ print(renpy.get_attributes("oveja"))
    $ mensaje=renpy.input("Insert you message here")
    $ a=esteganografia_escribir(mensaje,"images/oveja.png","images/output.png")
    e "Guardaste el mensaje en el siguiente archivo."
    show expression "images/output.png" at topright
    $ mensaje_foto=esteganografia_leer("output.png").leer_texto()
    e "El mensaje es el siguiente:"
    e "[mensaje_foto]"

    # This ends the game.

    return
