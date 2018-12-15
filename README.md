# Consulta de datos Banxico para el desafío Cumplo
Sistema desarrollado para entrevista de trabajo en Cumplo.  
Desarrollador: **Agustín Torres Munguía.**     
Fecha: **17 de diciembre de 2018.**

## Tecnología utilizada
- Python 3.7.1
- pip 18.1
- Django 2.1.4
- mysqlclient 1.3.14
- zeep 3.1.0
- lxml 4.2.5

## Estructura general del proyecto

Es un sistema muy básico donde la estructura es la siguiente:
- cumplovenv - Carpeta contenedora del espacio virtual.
- cumplochallenge - Proyecto general.
	- apps - Carpeta creada para dar orden y seccionar las aplicaciones de cada proyecto.
		- uids - aplicación contenedora de los métodos para cada petición.
	- templates - Carpeta donde almaceno las vistas (html) ligada para cada método del sistema.
