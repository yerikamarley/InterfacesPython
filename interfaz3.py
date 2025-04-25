import tkinter as tk     # Importamos Tkinter, la librería para interfaces
from tkinter import messagebox # Importamos el módulo de mensajes emergentes
import csv # Importamos el módulo CSV para manejar archivos CSV
# Importamos el módulo OS para manejar operaciones del sistema operativo
import os

def mostrar_interfaz3(nombre):
    # Creamos la ventana del formulario
    ventana = tk.Tk() # Inicializamos la ventana
    ventana.title("Formulario") # Título de la ventana
    ventana.geometry("500x420") # Tamaño de la ventana (ancho x alto)
    ventana.configure(bg="#171818")  # Fondo exterior oscuro

    # Contenedor del formulario
    frame = tk.Frame(ventana, bg="#2b2b2b", padx=20, pady=20) # Color del fondo interior
    # Colocamos el frame en el centro de la ventana
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Etiqueta principal
    etiqueta = tk.Label(    ## Etiqueta de texto
        frame,
        text=f"{nombre}, por favor completa este formulario:", # Mensaje de bienvenida
        font=("Segoe UI", 11, "bold"),  # Fuente del texto
        # Texto blanco
        fg="#ffffff",   ## Color del texto
        # Fondo igual al contenedor
        bg="#2b2b2b"
    )
    etiqueta.pack(pady=(0, 10)) # Espaciado inferior

    # Campo Edad
    tk.Label(frame, text="Edad:", font=("Segoe UI", 10), bg="#2b2b2b", fg="#ffffff").pack(anchor="w") # Etiqueta de Edad
    edad_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bg="#3c3c3c", fg="white", insertbackground="white") # Campo de entrada para Edad
    edad_entry.pack(pady=5) # Espacio debajo del campo de entrada

    # Campo Ciudad
    tk.Label(frame, text="Ciudad:", font=("Segoe UI", 10), bg="#2b2b2b", fg="#ffffff").pack(anchor="w") # Etiqueta de Ciudad3   
    ciudad_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bg="#3c3c3c", fg="white", insertbackground="white") # Campo de entrada para Ciudad3
    ciudad_entry.pack(pady=5)

    # Campo Correo
    tk.Label(frame, text="Correo:", font=("Segoe UI", 10), bg="#2b2b2b", fg="#ffffff").pack(anchor="w") # Etiqueta de Correo
    correo_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bg="#3c3c3c", fg="white", insertbackground="white")  # Campo de entrada para Correo
    # Campo de entrada para Correo
    correo_entry.pack(pady=5)

    # Campo Trabajo
    tk.Label(frame, text="Trabajo:", font=("Segoe UI", 10), bg="#2b2b2b", fg="#ffffff").pack(anchor="w") 
    trabajo_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bg="#3c3c3c", fg="white", insertbackground="white") # Campo de entrada para Trabajo
    # Campo de entrada para Trabajo
    trabajo_entry.pack(pady=5)

    # Pregunta: ¿Quiere recibir mensajes?
    tk.Label(frame, text="¿Desea recibir mensajes de información sobre servicios?", font=("Segoe UI", 10), bg="#2b2b2b", fg="#ffffff").pack(anchor="w", pady=(10, 0))

    recibir_mensajes = tk.StringVar(value="No")
    opciones = tk.Frame(frame, bg="#2b2b2b")
    opciones.pack(anchor="w", pady=5)
    tk.Radiobutton(opciones, text="Sí", variable=recibir_mensajes, value="Sí", bg="#2b2b2b", fg="white", selectcolor="#3c3c3c").pack(side="left", padx=10) # Opción "Sí"
    tk.Radiobutton(opciones, text="No", variable=recibir_mensajes, value="No", bg="#2b2b2b", fg="white", selectcolor="#3c3c3c").pack(side="left")

    # Función para guardar los datos
    def finalizar():
        edad = edad_entry.get()     ## Obtener la edad ingresada
        ciudad = ciudad_entry.get()   ## Obtener la ciudad ingresada
        correo = correo_entry.get() ## Obtener el correo ingresado
        trabajo = trabajo_entry.get() 
        mensajes = recibir_mensajes.get() ## Obtener la opción de mensajes

        if not edad or not ciudad or not correo or not trabajo: # Verificar si los campos están vacíos
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")  # Mensaje de advertencia
            return

        archivo = "datos_usuarios.csv"   # Nombre del archivo CSV
        archivo_existe = os.path.isfile(archivo) # Verificar si el archivo ya existe    

        with open(archivo, mode="a", newline='', encoding="utf-8") as file: # Abrir el archivo en modo de escritura3
            writer = csv.writer(file) # Crear un objeto escritor CSV

            if not archivo_existe: # Si el archivo no existe, escribir la cabecera
                writer.writerow(["Nombre", "Edad", "Ciudad", "Correo", "Trabajo", "Mensajes"])  # Cabecera del CSV
            writer.writerow([nombre, edad, ciudad, correo, trabajo, mensajes]) # Escribir los datos del usuario en el CSV

        messagebox.showinfo("Formulario enviado", f"Gracias {nombre}, tus datos han sido guardados.") # Mensaje de éxito
        ventana.destroy() # Cerrar la ventana actual
        # Aquí puedes agregar la lógica para redirigir a otra interfaz o realizar otra acción

    # Botón para finalizar
    tk.Button(
        frame, # Botón para finalizar
        text="Finalizar", # Texto del botón
        font=("Segoe UI", 10, "bold"),  
        bg="#317a11", # Verde sofisticado
        fg="white", # Texto blanco
        activebackground="#3c3c3c", # Color más oscuro al hacer clic
        activeforeground="white", # Texto blanco al hacer clic
        padx=10,        # Espacio horizontal del botón
        pady=5, # Espacio interno del botón
        relief="flat",  # Sin relieve para un diseño más limpio
        command=finalizar , # Llama a la función finalizar al hacer clic
    ).pack(pady=15)

    ventana.mainloop() # Mostramos la ventana
