import tkinter as tk  # Importamos Tkinter, la librería para interfaces
from interfaz2 import mostrar_interfaz2  # Traemos la siguiente pantalla

def mostrar_interfaz1():
    # Creamos la ventana principal de la aplicación
    ventana = tk.Tk() # Inicializamos la ventana
    ventana.title("Bienvenido a Yerika App")
    ventana.geometry("400x220")  # Tamaño de la ventana (ancho x alto)
    ventana.configure(bg="#171818")  # Color del fondo exterior

    # Creamos un contenedor centrado para la tarjeta visual
    frame = tk.Frame(ventana, bg="#2b2b2b", padx=10, pady=15) # Color del fondo interior
    frame.place(relx=0.5, rely=0.5, anchor="center") # Colocamos el frame en el centro de la ventana

    # Etiqueta de bienvenida con estilo elegante
    etiqueta = tk.Label(
        frame,
        text="¡Hola! Bienvenido a Aprendiendo con Yerika.\n¿Cuál es tu nombre?",
        font=("Segoe UI", 11, "bold"),
        fg="#ffffff",       # Texto blanco
        bg="#2b2b2b",       # Fondo igual al frame para armonía visual
        justify="center"    # Alineación centrada del texto
    )
    etiqueta.pack(pady=(0, 10))  # Espacio debajo de la etiqueta

    # Entrada de texto para capturar el nombre del usuario
    nombre = tk.StringVar()
    entrada = tk.Entry(
        frame,
        textvariable=nombre,
        font=("Segoe UI", 10),
        width=28,
        bd=1,
        relief="solid",
        justify="center",
        bg="#3c3c3c",         # Fondo oscuro para el campo de entrada
        fg="white",           # Texto blanco
        insertbackground="white"  # Cursor blanco
    )
    entrada.pack(pady=5)

    # Función que se ejecuta cuando se hace clic en el botón
    def siguiente():
        ventana.destroy() # Cierra la ventana actual
        # Llama a la siguiente interfaz y pasa el nombre ingresado
        mostrar_interfaz2(nombre.get()) # Llama a la siguiente interfaz y pasa el nombre ingresado

    # Botón para continuar
    boton = tk.Button(
        frame,
        text="Siguiente", # Texto del botón
        font=("Segoe UI", 10, "bold"), # Fuente del botón
        bg="#317a11",             # Gris medio
        fg="white",            # Texto blanco
        activebackground="#3c3c3c",  # Al hacer clic, se pone más oscuro
        activeforeground="white", # Texto blanco al hacer clic
        padx=10,         # Espacio horizontal del botón
        pady=4, # Espacio interno del botón
        relief="flat",  # Sin relieve para un diseño más limpio
        command=siguiente,  # Llama a la función siguiente al hacer clic
        cursor="hand2"      # Cambia el cursor al pasar por encima
    )
    boton.pack(pady=12) # Espacio debajo del botón

    # Mostramos la ventana
    ventana.mainloop()
