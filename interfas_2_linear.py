import tkinter as tk
import serial

ser = serial.Serial("COM7", 9600)

root = tk.Tk()
root.title("Stepper Motor Control")

def on_slider_change(val):
    ser.write(str(int(val)).encode())

def on_add_clicked():
    current_val = int(slider.get())
    slider.set(current_val + 1)
    ser.write(str(int(current_val + 1)).encode())

def on_subtract_clicked():
    current_val = int(slider.get())
    slider.set(current_val - 1)
    ser.write(str(int(current_val - 1)).encode())

slider = tk.Scale(root, from_=0, to=1900, orient="horizontal", length=1200, command=on_slider_change)
slider.pack()

add_button = tk.Button(root, text="+", command=on_add_clicked)
add_button.pack()

subtract_button = tk.Button(root, text="-", command=on_subtract_clicked)
subtract_button.pack()

position_label = tk.Label(root, text="Position:")
position_label.pack()

root.mainloop()
