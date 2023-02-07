
import PySimpleGUI as sg
from gpiozero import LED,PWMLED

led = PWMLED(16) 
relay = LED(27)

layout =[[sg.Text("raspi gui controler", font=("Helvetica",30))],
        [sg.Button("Ligth",button_color="white on red", font=("Helvetica",75),pad=(5,5),key="-B-")],
        [sg.Slider(range=(0,10), default_value=10, orientation="h", key="brightness",size=(40,30),enable_events=True)],
        [sg.Button("relay",font=("Helvetica"),pad=(5,5),button_color="white on red ",key="-B2-" )],
        [sg.Exit()]]    

window = sg.Window("togle boton exemple",layout, size=(600,380), element_justification="center", finalize=True)
window.Maximize()
down= False
b2down=False

while True:
    event, values = window.read()
    print(event,values)
    if event in (sg.WIN_CLOSED,"exit"):
        led.off()
        relay.off()
        break
    elif event == "-B-":
        dow =not down
        window["-B-"].update(button_color="white on green" if dow else "white on red")
        if dow:
            window["brightness"].update(10)
            led.value = 1
        else:
            led.off()
    elif event =="-B2-":
        b2down = not b2down
        window["-B-"].update(button_color="white on green"if b2down else "white on red")
        if b2down:
            relay.on()
        else :
            relay.off()                
    elif event == "brightness":
        if down:
            led.value = values["brightness"]/10
window.close()                    