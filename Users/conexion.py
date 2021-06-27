# -*- coding: utf-8 -*-
"""
Created on Sun May 30 16:34:09 2021

@author: Izhak
"""
import mysql.connector


def connection():
    
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        database="proyecto_master",
        port = 3306
    )
    
    mycursor = db.cursor(buffered = True)
    
    return [db, mycursor]


