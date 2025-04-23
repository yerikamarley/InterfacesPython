import tkinter as tk
from tkinter import messagebox
import csv
import os

def mostrar_interfaz3(nombre):
    #  Creamos la ventana del formulario
    ventana = tk.Tk()
    ventana.title("Formulario")
    ventana.geometry("500x350")
    ventana.configure(bg="#eaf4f4")  # Fondo claro

    # 🪟 Contenedor centrado para el formulario
    frame = tk.Frame(ventana, bg="#d6eaea", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # 👤 Mensaje inicial personalizado
    etiqueta = tk.Label(
        frame,
        text=f"📋 {nombre}, por favor completa este formulario:",
        font=("Segoe UI", 12, "bold"),
        fg="#175558",
        bg="#d6eaea"
    )
    etiqueta.pack(pady=(0, 10))

    #  Campo Edad
    tk.Label(frame, text="Edad:", font=("Segoe UI", 10), bg="#d6eaea", fg="#175558").pack(anchor="w")
    edad_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30)
    edad_entry.pack(pady=5)

    # Campo Ciudad
    tk.Label(frame, text="Ciudad:", font=("Segoe UI", 10), bg="#d6eaea", fg="#175558").pack(anchor="w")
    ciudad_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30)
    ciudad_entry.pack(pady=5)

    #  Campo Correo
    tk.Label(frame, text="Correo:", font=("Segoe UI", 10), bg="#d6eaea", fg="#175558").pack(anchor="w")
    correo_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30)
    correo_entry.pack(pady=5)

    #  Función para guardar los datos
    def finalizar():
        edad = edad_entry.get()
        ciudad = ciudad_entry.get()
        correo = correo_entry.get()

        if not edad or not ciudad or not correo:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return

        archivo = "datos_usuarios.csv"
        archivo_existe = os.path.isfile(archivo)

        with open(archivo, mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if not archivo_existe:
                writer.writerow(["Nombre", "Edad", "Ciudad", "Correo"])
            writer.writerow([nombre, edad, ciudad, correo])

        messagebox.showinfo("Formulario enviado", f"¡Gracias {nombre}!\nTus datos han sido guardados.")
        ventana.destroy()

    #  Botón para finalizar y guardar datos
    tk.Button(
        frame,
        text="💾 Finalizar",
        font=("Segoe UI", 11, "bold"),
        bg="#3b8686",
        fg="white",
        activebackground="#175558",
        activeforeground="white",
        padx=10,
        pady=5,
        relief="flat",
        command=finalizar
    ).pack(pady=15)

    ventana.mainloop()
