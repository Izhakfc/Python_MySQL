# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:36:10 2021

@author: Izhak
"""

from datetime import datetime
import hashlib
import Users.conexion as conexion

# Acceso reducido a SQL con conexion
conectar = conexion.connection()
db = conectar[0]
mycursor = conectar[1]

class Usuarios():
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def register(self):
        # Cifrar contraseña (Cambio tambien en tabla)
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), datetime.now())
        
        try:
            mycursor.execute(sql,usuario)
            db.commit()  
            result = [mycursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
    
    def identify(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s" 
        
        # Consulta para comprobar si existe el usuario
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        mycursor.execute(sql,usuario)
        result = mycursor.fetchone()
        
        return result