from tkinter import *
from tkinter import messagebox
import sqlite3
from licencia import Licencia

#Ejercicio de base de datos con conexion sqlite 3, funciona bien, nada mas que es muy
#poco util si se tienen que poner mas aceptamientos, pero para empezar a darse una idea
#viene bastante bien. se usan las librerias de TKINTER,SQLITE3 Y DBbroser para ver la 
#tabla.

def conexionBBDD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	
	try:

		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD","BBDD Creada con exito")

	except:
		messagebox.showwarning("Atencion","La base de datos ya existe")

#------------------Salir de la aplicacion----------------------------

def salirAplicacion():
	valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()

#------------------Borrar campos--------------------------------------

def limpiarCampos():
	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textoComentario.delete(1.0,END)
	"""1.0",END)+"')"""

#-------------------Crear-----------------------------------------------
def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+
		"','"+miPass.get()+ 
		"','"+miApellido.get()+
		"','"+miDireccion.get()+
		"','"+textoComentario.get("1.0",END)+"')")
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con exito")

#---------------------Leer-----------------------------------------------
def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	elUsuario=miCursor.fetchall()
	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0,usuario[5])
	miConexion.commit()
#-----------------------Actualizar---------------------------------------
def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='"+ miPass.get() +
		"', APELLIDO='"+ miApellido.get() +
		"', DIRECCION='"+ miDireccion.get() +
		"', COMENTARIOS='"+ textoComentario.get("1.0",END)+
		"' WHERE ID=" + miId.get()) 	
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con exito")

#------------------------Eliminar---------------------------------------

def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro borrado con exito")

#--------------------------------------------------------------------

root=Tk()

miFrame=Frame(root,width=1200,height=600)

miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

#-----------------Barra Menu----------------------------------------

barraMenu=Menu(root)

root.config(menu=barraMenu,width=300,height=300)

archivoBBCO=Menu(barraMenu,tearoff=0)
archivoBBCO.add_command(label="Conectar",command=conexionBBDD)
archivoBBCO.add_command(label="Salir",command=salirAplicacion)

archivoBuscar=Menu(barraMenu,tearoff=0)
archivoBuscar.add_command(label="Borrar Campos",command=limpiarCampos)

archivoCRUD=Menu(barraMenu,tearoff=0)
archivoCRUD.add_command(label="Crear",command=crear)
archivoCRUD.add_command(label="Leer",command=leer)
archivoCRUD.add_command(label="Actualizar",command=actualizar)
archivoCRUD.add_command(label="Borrar",command=eliminar)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=Licencia)

#----------------------------------------------------------------

barraMenu.add_cascade(label="BBCO",menu=archivoBBCO)
barraMenu.add_cascade(label="Borrar",menu=archivoBuscar)
barraMenu.add_cascade(label="CRUD",menu=archivoCRUD)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

#---------------Titulo de la aplicacion--------------------------

root.title("Archivero SQLite3")
root.iconbitmap("Icon.ico")

#---------------Cuadros de Textos-------------------------------

cuadroID=Entry(miFrame,textvariable=miId)
cuadroID.grid(row=1,column=2)

LabelID=Label(miFrame,text="Id: ")
LabelID.grid(row=1,column=1,sticky="e",padx=10,pady=10)

#-------------------------------------

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=2,column=2)
cuadroNombre.config(fg="red",justify="right")

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=2,column=1,padx=10,pady=10)

#-------------------------------------

cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=3,column=2)
cuadroPass.config(show="*")

passLabel=Label(miFrame,text="Contraseña: ")
passLabel.grid(row=3,column=1,padx=10,pady=10)

#-------------------------------------

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=4,column=2)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=4,column=1,padx=10,pady=10)

#------------------------------------

cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=5,column=2)

direccionLabel=Label(miFrame,text="Domicilio: ")
direccionLabel.grid(row=5,column=1,padx=10,pady=10)

#-------------------------------

cuadroComentarios=Entry(miFrame)
cuadroComentarios.grid(row=6,column=2)

comentarioLabel=Label(miFrame,text="Comentarios: ")
comentarioLabel.grid(row=6,column=1,padx=10,pady=10)

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=6,column=2,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=6,column=3,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#-----------------Botonera de abajo------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2,text="Crear",command=crear)
botonCrear.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer",command=leer)
botonLeer.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Modificar",command=actualizar)
botonActualizar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

botonBorrar=Button(miFrame2,text="Eliminar",command=eliminar)
botonBorrar.grid(row=1,column=4,sticky="e",padx=10,pady=10)

#...................................................................
root.mainloop()