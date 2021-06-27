# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:33:25 2021

@author: Izhak
"""

import Users.usuarios as user
import Notas.acciones
from sys import exit

class Acciones():
    
    def Registro(self):
            print("\nComenzando registro en el sistema...")
            nombre = input("Introduce tu nombre: ")
            apellidos = input("Introduce tus apellidos: ")
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            
            username = user.Usuarios(nombre, apellidos, email, password)
            registro = username.register()
            
            if registro[0] >= 1:
                print(f'\nPerfecto! {username.nombre}, te has registrado con el email: {username.email}')
            else:
                print("\nNo se ha podido registrar correctamente...")
    def Login(self):
           print("\nIdentificacion de usuario requerida...")
           
           try:
               email = input("Introduce tu email: ")
               password = input("Introduce tu contraseña: ")
               
               # Solo creas sujeto con email y password por que son los necesarios para hacer el Login
               usuario = user.Usuarios('', '', email, password)
               login = usuario.identify()
               
               if email == login[3]:
                   print(f'\nBienvenido {login[1]} has iniciado sesión con el correo {login[3]}')
                   self.posterior_actions(login)
               
           except ZeroDivisionError as e:
               print(type(e))
               print(type(e).__name__)
               print('Email o contraseña incorrecta! Intentar de nuevo')
  
           
   
    def posterior_actions(self, usuario):
        print("""
                ====================================
                =    Acciones disponibles          =
                =                                  =
                =    -Crear nota (crear)           =
                =    -Mostrar tus notas (mostar)   =
                =    -Eliminar nota (eliminar)     =
                =    -Salir (salir)                =
                ====================================
              """)
        accion = input("Selecciona una acción: ")
        do = Notas.acciones.Acciones()
        
        if accion == "crear":
            print("\nIniciando creación de nota ...")
            do.create(usuario)
            self.posterior_actions(usuario)
        elif accion == "mostrar":
            do.mostrar(usuario)
            print("\nMostrando nota ...")
            self.posterior_actions(usuario)
        elif accion == "eliminar":
            do.delete(usuario)
            print("\nEliminando nota ...")
            self.posterior_actions(usuario)
        elif accion == "salir":
            print(f'Hasta luego {usuario[1]}!!')
            exit()    
        
       # return None
