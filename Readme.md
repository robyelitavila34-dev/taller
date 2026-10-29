Modulos usados 
urls.py dentro de proyectoparcial
funcion este archivo cumple como la puerta de entrada cuando hacemos la peticion que necesitamos 
este archivo es el que abre primero django para saber de donde es la peticion 

urls.py dentro de Applist
Este módulo es fundamental porque une la dirección web exacta que tiene la logioca de python 

views.py dentro de Applist
este modulo es el que le da vida a los metodos ya que gracias a este modulo traduce las peticiones de HTTP del mundo exterior 

probar_api.py
En lugar de usar una aplicación externa como Postman o Insomnia para probar tu API, este script hace exactamente el mismo trabajo, pero lo ejecuta de forma automática con solo correrlo desde tu terminal. Utiliza las librerías nativas de Python (urllib y json) para comunicarse con tu servidor de Django sin necesidad de instalar paquetes adicionales.

recursos utilizados 
https://docs.djangoproject.com/en/6.1/ref/request-response/
https://docs.djangoproject.com/en/6.1/topics/class-based-views/
https://docs.djangoproject.com/en/6.1/ref/request-response/#:~:text=Django%20uses%20request%20and%20response%20objects%20to%20pass,as%20the%20first%20argument%20to%20the%20view%20function.
