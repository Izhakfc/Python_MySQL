# -*- coding: utf-8 -*-
"""
Created on Sun May 30 01:36:18 2021

@author: Izhak
"""
from Users import conexion as conexion

connect = conexion.connection()
db = connect[0]
mycursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        
    def Save(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        mycursor.execute(sql, nota)
        db.commit()
        
        return [mycursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        
        return result
    
    def eliminate(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} and titulo LIKE '%{self.titulo}%'"
        
        mycursor.execute(sql)
        db.commit()
        
        return[mycursor.rowcount,self]