#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

r="s"

while r=="s":
	lista=[]
	rayitas=[]
	letras=[]
	pistas=[]

	sp=spotipy.Spotify()

	try:
		os.system('cls')
		print "\t\t\tAHORCADO"
		artista=raw_input("Ingresa el nombre de alguna banda o solista: ")

		resultados=sp.search(q=artista, limit=30)

		for t in resultados['tracks']['items']:
			cancion=elimina_tildes(t['name'])
			pistas.append(t['album']['name'])
			lista.append(cancion.lower())

		palabra=random.choice(lista)

		for t in range(30):
			if palabra==lista[t]:
				pista=pistas[t]

		comparar=palabra
		palabra.split()
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
			os.system('cls')
			print "\t\t\tAHORCADO"
			print AHORCADO[i]+"\n"

			if x>0:
				print "El album donde aparece la cancion es: "+pista+"\n"

			if u>0:
				print "letras usadas: "
				print letras

			for j in range(0,p):
				print rayitas[j],

			letra=raw_input("\n\nIngrese una letra: ")

			if letra=='pista':
				x+=1
				if x>1:
					i+=1
			else:
				letras.append(letra)

				if letra==comparar:
					break
				elif letra in comparar:
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

		os.system('cls')
		if i==7:
			print AHORCADO[i]+"\n"
			print "\nFin del juego"
			print "\nEl nombre de la cancion era: "+palabra
		else:
			print AHORCADO[8]+"\n"
			print "\n"+palabra
			print "\nFelicidades adivinaste la cancion"
		r=raw_input("\nDeseas volver a jugar (s/n)? ")
	except IndexError:
		print("Lo sentimos el artista no existe")
		r=raw_input("\nDeseas volver a intentarlo (s/n)? ")
		