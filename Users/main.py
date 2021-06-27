# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:34:38 2021

@author: Izhak
"""

"""
Proyecto Python y MySQL
- Abrir asistente
- Login o registro
- Si se selecciona registro, creará un usuario en la base de datos
- Si se selecciona login, idenfica al usuario y muestra opciones
- Crear nota, mostrar nota, borrar nota
"""
from Users import acciones

print("""
           ===============================
           =    Acciones disponibles     =
           =                             =
           =    -Registro                =
           =    -Login                   =
           =                             =
           ===============================
      """)
      
Do = acciones.Acciones()
accion = input("Seleccione una opcion: ")

if accion == "Registro":
    Do.Registro()
elif accion == "Login":
    Do.Login()
else:
    print("\nComando no reconocido")
    