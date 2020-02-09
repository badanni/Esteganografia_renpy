#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  esteganografia.rpy
#  
#  Copyright 2020 badanni <dannyvasconeze@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# basado en https://github.com/parzibyte/esteganografia-python

init python:
    import pygame
    class esteganografia_escribir(object):
      def __init__(self,mensaje,fname,fname_out="output.png"):
        self.caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]
        self.ocultar_texto(mensaje,fname,fname_out)
      def obtener_lista_de_bits(self,texto):
       lista = []
       for letra in texto:
         representacion_ascii = ord(letra)
         representacion_binaria =  bin(representacion_ascii)[2:].zfill(8)
         for bit in representacion_binaria:
             lista.append(bit)
       for bit in self.caracter_terminacion:
          lista.append(bit)
       return lista
      def cambiar_ultimo_bit(self,byte, nuevo_bit):
        return byte[:-1] + str(nuevo_bit)
      def modificar_color(self,color_original, bit):
        color_binario = bin(color_original)[2:].zfill(8)
        color_modificado = self.cambiar_ultimo_bit(color_binario, bit)
        return int(color_modificado, 2)
      def ocultar_texto(self,mensaje,fname,fname_out):
        a=renpy.file(fname)
        b=im.Data(a,fname)
        #surface_pygame=im.load_surface(b)
        surface=renpy.display.pgrender.load_image(renpy.loader.load(fname), fname)
        dimensiones=surface.get_size()
        anchura=dimensiones[0]
        altura=dimensiones[1]
        lista = self.obtener_lista_de_bits(mensaje)
        contador = 0
        longitud = len(lista)
        for x in range(anchura):
            for y in range(altura):
              if contador < longitud:
                pixel = surface.get_at((x,y))
                rojo=pixel[0]
                verde=pixel[1]
                azul=pixel[2]
                alfa=pixel[3]
                
                if contador < longitud:
                    rojo_modificado = self.modificar_color(rojo, lista[contador])
                    contador += 1
                else:
                    rojo_modificado = rojo
                if contador < longitud:
                    verde_modificado = self.modificar_color(verde, lista[contador])
                    contador += 1
                else:
                    verde_modificado = verde
                if contador < longitud:
                    azul_modificado = self.modificar_color(azul, lista[contador])
                    contador += 1
                else:
                    azul_modificado = azul
                if contador < longitud:
                    alfa_modificado = self.modificar_color(alfa, lista[contador])
                    contador += 1
                else:
                    alfa_modificado = alfa
                surface.set_at((x,y),(rojo_modificado, verde_modificado, azul_modificado,alfa_modificado))
              else:
                break
            else:
              continue
            break
        if contador >= longitud:
            print("Mensaje escrito correctamente")
        else:
            #print("Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres".format( math.floor((longitud - contador) / 8) ))
            renpy.error("Supero las dimensiones de la imagen; contador= %s" % contador)
        direccion=config.gamedir
        pygame.image.save(surface,direccion.replace("\\","/")+"/output.png")
    class esteganografia_leer(object):
      def __init__(self,fname):
        self.caracter_terminacion = "11111111"
        self.fname=fname
      def obtener_lsb(self,byte):
        return byte[-1]
      def obtener_representacion_binaria(self,numero):
        return bin(numero)[2:].zfill(8)
      def binario_a_decimal(self,binario):
        return int(binario, 2)
      def caracter_desde_codigo_ascii(self,numero):
        return chr(numero)
      def leer_texto(self):
        fname=self.fname
        a=renpy.file(fname)
        b=im.Data(a,fname)
        #surface_pygame=im.load_surface(b)
        surface=renpy.display.pgrender.load_image(renpy.loader.load(fname), fname)
        dimensiones=surface.get_size()
        anchura=dimensiones[0]
        altura=dimensiones[1]
        byte = ""
        mensaje = ""
        for x in range(anchura):
            for y in range(altura):
                pixel = surface.get_at((x,y))
                rojo=pixel[0]
                verde=pixel[1]
                azul=pixel[2]
                alfa=pixel[3] # alpha sin uso
                
                byte += self.obtener_lsb(self.obtener_representacion_binaria(rojo))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""
                byte += self.obtener_lsb(self.obtener_representacion_binaria(verde))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""
                byte += self.obtener_lsb(self.obtener_representacion_binaria(azul))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""
                byte += self.obtener_lsb(self.obtener_representacion_binaria(alfa))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    mensaje += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""
            else:
                continue
            break
        return mensaje
        
    a=esteganografia_escribir("hola como estas?","oveja2.png","output.png")
    print(esteganografia_leer("output.png").leer_texto())
