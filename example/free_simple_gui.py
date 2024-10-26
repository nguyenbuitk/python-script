import FreeSimpleGUI as sg

layout = [
    [sg.Text("Enter your name:")],
    [sg.InputText(key='name')],
    # when click button "Exit" -> event = Exit
    [sg.Button("Greet"), sg.Button("Exit")]
]

window = sg.Window("Simple Event Example", layout)

while True:
    event, values = window.read()
    print("event: ", event)
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    if event == "Greet":
        sg.popup(f"Hello, {values['name']}!", title="Greeting")

window.close()