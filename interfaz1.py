import tkinter as tk
from interfaz2 import mostrar_interfaz2

def mostrar_interfaz1():
    ventana = tk.Tk()
    ventana.title("Bienvenido a Yerika App 💖")
    ventana.geometry("500x300")
    ventana.configure(bg="#eaf4f4")  # Fondo claro y limpio

    # Contenedor central (como una tarjetita suave)
    frame = tk.Frame(ventana, bg="#d6eaea", padx=20, pady=20, relief="flat", bd=2)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Etiqueta principal con estilo
    etiqueta = tk.Label(
        frame,
        text="👋 ¡Hola! Bienvenido a Aprendiendo con Yerika.\n Cuál es tu nombre?",
        font=("Segoe UI", 12, "bold"),
        fg="#175558",
        bg="#d6eaea",
        justify="center"
    )
    etiqueta.pack(pady=(0, 10))

    # Entrada de texto
    nombre = tk.StringVar()
    entrada = tk.Entry(
        frame,
        textvariable=nombre,
        font=("Segoe UI", 11),
        width=30,
        bd=1,
        relief="solid"
    )
    entrada.pack(pady=5)

    # Función que se ejecuta al dar clic en siguiente
    def siguiente():
        ventana.destroy()
        mostrar_interfaz2(nombre.get())

    # Botón estilizado
    boton = tk.Button(
        frame,
        text=" Siguiente",
        font=("Segoe UI", 11, "bold"),
        bg="#3b8686",
        fg="white",
        activebackground="#175558",
        activeforeground="white",
        padx=10,
        pady=5,
        relief="flat",
        command=siguiente
    )
    boton.pack(pady=10)

    ventana.mainloop()
