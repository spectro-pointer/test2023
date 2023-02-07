import tkinter as tk
import serial

ser = serial.Serial('COM7', 9600)

def send_steps(step):
    ser.write(str(step).encode())

def set_position_1():
    send_steps(position_1.get())

def set_position_2():
    send_steps(position_2.get())

def set_position_3():
    send_steps(position_3.get())

root = tk.Tk()
root.title("Control Motor Paso a Paso")

position_1 = tk.IntVar()
position_2 = tk.IntVar()
position_3 = tk.IntVar()

slider = tk.Scale(root, from_=0, to=1900, orient="horizontal",  length=1800, variable=position_1)
slider.pack()

button_1 = tk.Button(root, text="Posición 1", command=set_position_1)
button_1.pack()

button_2 = tk.Button(root, text="Posición 2", command=set_position_2)
button_2.pack()

button_3 = tk.Button(root, text="Posición 3", command=set_position_3)
button_3.pack()

root.mainloop()
