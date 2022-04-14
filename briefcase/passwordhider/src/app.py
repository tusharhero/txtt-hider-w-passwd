"""
hides text using a password and also unhides using the same.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from driver import encrypt
#I know the code is trash but I am not going to explain it(for now)
def win(start):
    box = toga.Box()
    tinput = toga.TextInput(placeholder="Enter the text.")
    pinput = toga.TextInput(placeholder="Enter the Password.")
    def output(dummy):
        e = encrypt(tinput.value,pinput.value)
        out = toga.Label(e)
        box.add(out)
    button = toga.Button("click me",on_press=output)
    box.add(tinput,pinput,button)
    return box

def main():
    return toga.App(startup=win)
