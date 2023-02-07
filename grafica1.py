import tkinter.filedialog
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def graficar():
  # Obtener el nombre del archivo seleccionado
  archivo = archivo_seleccionado.get()

  # Leer los datos del archivo y almacenarlos en dos listas
  x, y = np.loadtxt(archivo, skiprows=2, usecols=[0, 1], unpack=True)

  # Graficar los datos
  plt.title("Gráfica de espectros")
  plt.xlabel("Longitud de onda")
  plt.ylabel("Intensidad")
  plt.plot(x, y, "r")
  plt.show()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar archivo y graficar espectros")

# Crear una etiqueta para indicar al usuario qué debe hacer
etiqueta = tk.Label(ventana, text="Selecciona un archivo .txt para graficar los espectros:")
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
