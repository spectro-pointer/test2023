import re
import tkinter.filedialog
import tkinter as tk
import matplotlib.pyplot as plt

def graficar():
  # Obtener el nombre del archivo seleccionado
  archivo = archivo_seleccionado.get()
  
  # Leer los datos del archivo y almacenarlos en una lista
  with open(archivo, 'r') as f:
    datos = []
    for linea in f:
      # Verificar si la línea solo contiene números y puntos decimales
      if re.match(r"^[\d.]+$", linea):
        # Convertir la línea a número flotante y agregarla a la lista
        datos.append(float(linea))
  
  # Graficar los datos
  plt.plot(datos)
  plt.show()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar archivo y graficar datos")

# Crear una etiqueta para indicar al usuario qué debe hacer
etiqueta = tk.Label(ventana, text="Selecciona un archivo .txt para graficar sus datos:")
etiqueta.pack()

# Crear un cuadro de texto para mostrar el nombre del archivo seleccionado
archivo_seleccionado = tk.StringVar()
cuadro_texto = tk.Entry(ventana, textvariable=archivo_seleccionado)
cuadro_texto.pack()

# Crear un botón para abrir una ventana de diálogo de archivos
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=lambda: archivo_seleccionado.set(tk.filedialog.askopenfilename()))
boton_seleccionar.pack()





# Crear un botón para graficar los datos del archivo seleccionado
boton_graficar = tk.Button(ventana, text="Graficar", command=graficar)
boton_graficar.pack()

# Mostrar la ventana
ventana.mainloop()
