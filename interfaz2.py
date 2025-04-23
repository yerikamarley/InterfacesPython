import tkinter as tk
from interfaz3 import mostrar_interfaz3

def mostrar_interfaz2(nombre):
    #  Creamos una nueva ventana
    ventana = tk.Tk()
    ventana.title("Más sobre ti")
    ventana.geometry("500x300")
    ventana.configure(bg="#eaf4f4")  # Fondo suave lavanda claro

    #  Contenedor estilo tarjeta
    frame = tk.Frame(ventana, bg="#d6eaea", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    #  Mensaje personalizado con color y fuente linda
    mensaje = f"👤 Hola {nombre}, bienvenido nuevamente.\nQueremos saber más de ti \nResponde las preguntas a continuación:"
    etiqueta = tk.Label(
        frame,
        text=mensaje,
        font=("Segoe UI", 12, "bold"),
        fg="#175558",
        bg="#d6eaea",
        justify="center"
    )
    etiqueta.pack(pady=(0, 20))

    #  Función que va a abrir el formulario
    def siguiente():
        ventana.destroy()
        mostrar_interfaz3(nombre)

    #  Botón estilizado
    boton = tk.Button(
        frame,
        text="✨ Siguiente",
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
    boton.pack()

    #  Muestra la ventana
    ventana.mainloop()
