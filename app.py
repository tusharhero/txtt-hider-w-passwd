'''
Attempt at a GUI for people who can't stand a terminal.
'''
import PySimpleGUI as sg

from driver import encrypt
from driver import decrypt

#I know this app's code looks terrible and it doesn't have good comments but I don't have time to continue

sg.change_look_and_feel('DarkAmber')# Add a touch of color

# All the stuff inside your window.
buttons = [sg.Button('Hide text'),sg.Button('Unhide text')]
dialogs = [sg.Multiline('text',expand_x=True,expand_y=True,key='text'), sg.Multiline('Hidden text',expand_x=True,expand_y=True,key= 'htext')]
layout = [
    [sg.Text('Only spaces, or uppercase or numbers and special characters other than ".,"')],
    [sg.Text('password:'), sg.InputText('password',expand_x=True)],
    buttons,
    dialogs,
    [sg.Button("Don't know what is going? Click me!",expand_x=True,key="help")]
    ]
readme = "This is a GUI implementation of txtt-hider-w-passwd. \n\n\n The Box on the right contains the legible text that you may want to hide using the password, it also contains any output from unhiding text. The same goes for the one in the right.\n\n\n Copyright © 2022 Tushar Maharana, https://tusharhero.github.io/ \n\n LICENSE: The MIT License (MIT)"
# Create the Window
window = sg.Window('txtt-hider-w-passwd',layout,size=(900 ,600),resizable=True, element_justification='center',font="Arial") 


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
    if event == 'help':
        sg.popup(readme)
window.close()
'''    

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)
'''
