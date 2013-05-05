#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Ejercicio 1
# Desarrollar un programa que imprima tablas de multiplicar a partir de
# 3 parámetros recibidos por el usuario. El primer parámetro indicará 
# hasta que tabla debe imprimir. Los otros dos parametros serviran para
# delimitar el inicio y el fin de la tabla.

def main():
	
	m = input("Hasta qué tabla quiere calcular? ")
	i = input("Número inicial? ")
	f = input("Número final? ")
	
	tablas(m, i, f)	

def tablas(maximo, inicio, fin):

	for x in range(maximo):
		print ""
		
		for y in range(inicio, fin + 1):
			print (x + 1), "x", y, "=", (x + 1) * y
	
main()
