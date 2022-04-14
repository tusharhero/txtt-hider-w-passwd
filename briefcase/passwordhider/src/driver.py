from passwdhide import stringdecrypt
from passwdhide import stringencrypt

def encrypt(Message,password):
    cid = open("src/unicode.txt",'rt')#always use the same cid for the the password i'e uncide.txt from this repo
    cid = cid.read()
    dic = "abcdefghijklmnopqrstuvwxyz 1234567890.,"
    return stringencrypt(Message, password, dic, cid)





'''
print("passwdhide driver")
print("NO spaces, or uppercase or numbers and special characters other that ' '")
print("hit enter to continue")
input()
from passwdhide import stringdecrypt
from passwdhide import stringencrypt

cid = open("unicode.txt",'rt')#always use the same cid for the the password i'e uncide.txt from this repo
cid = cid.read()
dic = "abcdefghijklmnopqrstuvwxyz 1234567890.,"

ask = input("do you want to encrypt or decrypt? : e or d")
if ask == "e":
    print("encrypting...")
    Message = input("Message:")
    password = input("password: ")
    print(stringencrypt(Message, password, dic, cid))
if ask == "d":
    print("decrypting...")
    cryptedmessage = input("Hidden Message: ")
    password = input("password: ")
    print(stringdecrypt(cryptedmessage, password, dic, cid))
'''