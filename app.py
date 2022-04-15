import PySimpleGUI as sg

from driver import encrypt
from driver import decrypt

sg.theme('DarkBlue2')   # Add a touch of color

# All the stuff inside your window.
buttons = [sg.Button('Hide text'),sg.Button('Unhide text')]
dialogs = [sg.Multiline('text',expand_x=True,expand_y=True,key='text'), sg.Multiline('Hidden text',expand_x=True,expand_y=True,key= 'htext')]
layout = [
    [sg.Text('Only spaces, or uppercase or numbers and special characters other than ".,"')],
    [sg.Text('password:'), sg.InputText('password',expand_x=True)],
    buttons,
    dialogs
    ]
# Create the Window
window = sg.Window('txtt-hider-w-passwd', layout,size=(600 ,450)) 


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    #print(values)
    #print(values[1])
    if event == 'Hide text':
        window['htext'].update(encrypt(values['text'],values[0]))
    if event == 'Unhide text':
        window['text'].update(decrypt(values['htext'],values[0]))
window.close()