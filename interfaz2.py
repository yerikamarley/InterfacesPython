import tkinter as tk
from interfaz3 import mostrar_interfaz3  # Importamos la siguiente pantalla

def mostrar_interfaz2(nombre):
    # Creamos una nueva ventana
    ventana = tk.Tk()  # Inicializamos la ventana
    ventana.title("Más sobre ti") # Título de la ventana
    ventana.geometry("500x280") # Tamaño de la ventana (ancho x alto)
    ventana.configure(bg="#171818")  # Fondo exterior oscuro

    # Contenedor interno estilo tarjeta
    frame = tk.Frame(ventana, bg="#2b2b2b", padx=5, pady=15) # Color del fondo interior
    frame.place(relx=0.5, rely=0.5, anchor="center")    # Colocamos el frame en el centro de la ventana

    # Mensaje de bienvenida personalizado con estilo sobrio
    mensaje = f"Hola {nombre}, bienvenido nuevamente.\nQueremos saber más de ti.\nResponde las preguntas a continuación:"   # Texto de bienvenida
    etiqueta = tk.Label( ## Etiqueta de texto
        frame, ## Contenedor del texto
        text=mensaje, # Mensaje de bienvenida
        font=("Segoe UI", 11, "bold"), # Fuente del texto
        fg="#ffffff",     # Texto blanco
        bg="#2b2b2b",     # Fondo igual al contenedor
        justify="center" # Alineación centrada del texto
    )
    etiqueta.pack(pady=(0, 15))  # Espaciado inferior

    # Función que abrirá el formulario (interfaz3)
    def siguiente():    
        ventana.destroy() # Cierra la ventana actual
        # Llama a la siguiente interfaz y pasa el nombre ingresado
        mostrar_interfaz3(nombre) # Llama a la siguiente interfaz y pasa el nombre ingresado

    # Botón estilizado para continuar
    boton = tk.Button( # Botón para continuar
        frame, # Contenedor del botón
        # Texto del botón
        text="Siguiente",
        font=("Segoe UI", 10, "bold"),
        bg="#317a11",              # Verde sofisticado
        fg="white",           # Texto blanco    
        activebackground="#3c3c3c",  # Color más oscuro al hacer clic
        activeforeground="white", # Texto blanco al hacer clic
            
        padx=10, # Espacio horizontal del botón
        pady=5, # Espacio interno del botón
        relief="flat", # Sin relieve para un diseño más limpio
        command=siguiente, # Llama a la función siguiente al hacer clic
        cursor="hand2" # Cambia el cursor al pasar sobre el botón
    )
    boton.pack(pady=10) # Espacio debajo del botón

    # Mostramos la ventana
    ventana.mainloop()
