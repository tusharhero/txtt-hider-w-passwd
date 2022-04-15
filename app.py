import PySimpleGUI as sg

from driver import encrypt
from driver import decrypt

sg.theme('DarkBlue2')   # Add a touch of color

# All the stuff inside your window.
buttons = [sg.Button('Hide text'),sg.Button('Unhide text')]
layout = [
    [sg.Text('Only spaces, or uppercase or numbers and special characters other than ".,"')],
    [sg.Text('text/hidden text:'), sg.InputText('text or hiddentext',expand_x=True)],
    [sg.Text('password:'), sg.InputText('password',expand_x=True)],
    buttons,
    [[sg.Text('output:')],sg.Multiline('nothing here yet!',key='out',expand_x=True, expand_y=True)]
    ]
# Create the Window
window = sg.Window('txtt-hider-w-passwd', layout,size=(750 ,300)) 


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == 'Hide text':
        window['out'].update(encrypt(values[0],values[1]))
    if event == 'Unhide text':
        window['out'].update(decrypt(values[0],values[1]))
window.close()