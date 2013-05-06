#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Desafío 2

# Realizar una agenda de contactos
# cuando inicie el programa que te pregunte si quieres agregar contacto
# si se va a agregar un contacto, que pida nombre, teléfono y e-mail
# cuando termines te vuelve a preguntar si quieres agregar contacto
# si respondes no, muestra la lista de contactos y termina.

def main(): 
	
	sigue = input("Agregar contacto [si=1 / no=0]: ")		
		
	for x in range(sigue):
		nom = raw_input("Dame tu nombre: ")
		tel = raw_input("Dame tu teléfono: ")
		cor = raw_input("Dame tu correo: ")
		
		contatos = ""
		linea = "-" * 45
		
		contatos += linea + "\n" + linea + "\n" + "> " + nom + "\n" + "> " + tel + "\n" + "> " + cor + "\n"
	
	print contatos  

main()
		
