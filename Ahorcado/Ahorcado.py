#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Creado por: Luis Enrique Vite Aquino

import unicodedata
import spotipy
import random
import time
import sys
import os

AHORCADO = ['''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
      +---+
          |
      O   |
          |
          |
          |
    =========''', '''
      +---+
          |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
          |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
          |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
          |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
          |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
        +---+
            |
            |    
     \O/    |   
      |     |   
     < \    |
    =========''']

def elimina_tildes(s):    #Este metodo elimina las tildes de las letras devolviendonos el caracter sin estas
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

r="s"

while r=="s":
	lista=[]
	rayitas=[]
	letras=[]
	pistas=[]

	sp=spotipy.Spotify()  #creamos un objeto del tipo spotify

	try:
		os.system('cls')
		print "\t\t\tAHORCADO"
		artista=raw_input("Ingresa el nombre de alguna banda o solista: ")

		resultados=sp.search(q=artista, limit=30)     #Nos conectamos al api de spotify y hacemos una busqueda relacionada con el artista

		for t in resultados['tracks']['items']:       #Guardamos los track's encontrados en una lista para que despues se pueda escoger de manera aleatoria
			cancion=elimina_tildes(t['name'])
			pistas.append(t['album']['name'])         #Guardamos los nombres de los albunes de cada track guardado
			lista.append(cancion.lower())

		palabra=random.choice(lista)                  #Se escoge la cancion aleatoriamente

		for t in range(30):
			if palabra==lista[t]:
				pista=pistas[t]

		comparar=palabra
		palabra.split()                               #Separamos la palabra caracter por caracter 
		p=len(palabra)
		c=p

		for i in range (p):
			if(palabra[i]==' '):
				rayitas.append(' ')
				c=c-1
			elif(palabra[i]=='.'):
				rayitas.append('.')
				c=c-1
			elif(palabra[i]==','):
				rayitas.append(',')
				c=c-1
			elif(palabra[i]=='-'):
				rayitas.append('-')
				c=c-1
			elif(palabra[i]=='('):
				rayitas.append('(')
				c=c-1
			elif(palabra[i]=='°'):
				rayitas.append('°')
				c=c-1
			elif(palabra[i]=="'"):
				rayitas.append("'")
				c=c-1
			elif(palabra[i]=='"'):
				rayitas.append('"')
				c=c-1
			elif(palabra[i]==':'):
				rayitas.append(':')
				c=c-1
			else:
				rayitas.append('_') 

		i=0
		d=0
		u=0
		x=0

		while i<7:
			os.system('cls')                            #el comando permite limpiar la pantalla de la consola, si se trabaja en mac o linux es recomendable que se cambie el cls, por el comando que se utilize en su ditribucion
			print "\t\t\tAHORCADO"
			print AHORCADO[i]+"\n"

			if x>0:
				print "El album donde aparece la cancion es: "+pista+"\n"

			if u>0:
				print "letras usadas: "                   #despues de que el usuario halla ingresado una letra por primera vez el programa empezara a imprimir las letras utilizadas
				print letras

			for j in range(0,p):
				print rayitas[j],

			letra=raw_input("\n\nIngrese una letra: ")

			if letra=='pista':                                      #primero verifica si el usuario a escrito la palabra pista despues de la primera vez que lo hace empieza a contar como intento 
				x+=1
				if x>1:
					i+=1
			else:
				letras.append(letra)                                #agrega la letra utilizada por el usuario  a la lista letras 

				if letra==comparar:                                 #compara la cadena escrita por el usuario si es igual al nombre de la cancion entonces termina el ciclo
					break
				elif letra in comparar:                             #comprueba que la letra se encuente en el titulo de la cancion si es correcto cambia los _ por la letra en la lista rayitas
					for k in range(p):
						if letra==palabra[k]:
							rayitas[k]=letra
							d+=1
							u+=1
				else:
					i+=1
					u+=1
			if d==c:
				break

		os.system('cls')                        #el comando permite limpiar la pantalla de la consola, si se trabaja en mac o linux es recomendable que se cambie el cls, por el comando que se utilize en su ditribucion
		if i==7:
			print AHORCADO[i]+"\n"
			print "\nFin del juego"
			print "\nEl nombre de la cancion era: "+palabra
		else:
			print AHORCADO[8]+"\n"
			print "\n"+palabra
			print "\nFelicidades adivinaste la cancion"
		r=raw_input("\nDeseas volver a jugar (s/n)? ")          #pregunta si el usuario desea volver a jugar y si este escribe s entonces repite el ciclo anterior
	except IndexError:                                          #en dado caso de que el artista o banda no se encuentre en la base de datos de spotify le notifica al usuario y le pregunta si desea volver a intentar con otra busqueda
		print("Lo sentimos el artista no existe o no se encuentra en la base de datos de spotify")
		r=raw_input("\nDeseas volver a intentarlo (s/n)? ")
		