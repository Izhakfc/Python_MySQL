# -*- coding: utf-8 -*-
"""
Created on Tue May 25 22:11:47 2021

@author: Izhak
"""
import Notas.nota as modelo

class Acciones():
    def create(self, usuario):
       print(f'\nOk {usuario[1]} creando nueva nota ...')
       titulo = input('Introducir titulo: ')
       descripcion = input('Introducir contenido: ')
       
       nota = modelo.Nota(usuario[0], titulo, descripcion)
       guardado = nota.Save()
       
       if guardado[0] >= 1:
           print(f'\nSe ha guardado una nota: {nota.titulo}')
       else: 
            print(f'\n{usuario[1]} no se ha podido completar la accion')
            
    def mostrar(self, usuario):
        print(f'\nNotas del usuario {usuario[1]}: ')
        
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()
        
        for nota in notas:
            print("\n=====================================")
            print(nota[2])
            print(nota[3])
            print("=======================================")
    
    def delete(self,usuario):
        print("\nBorrando archivos del usuario {usuaurio[1]}...")
        
        titulo = input("Introducir el titulo de la nota a borrar: ")
        
        nota  = modelo.Nota(usuario[0], titulo,"")
        eliminar = nota.eliminate()
        
        if eliminar[0] >= 1:
            print(f"Se ha eliminado la nota {nota.titulo}")
        else:
            print("No se ha podido completar la accion ")