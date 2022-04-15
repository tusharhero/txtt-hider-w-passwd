#print("passwdhide driver")
#print("NO spaces, or uppercase or numbers and special characters other that ' '")
#print("hit enter to continue")
#input()
from passwdhide import stringdecrypt
from passwdhide import stringencrypt
def encrypt(Message, password):
    cid = open("unicode.txt",'rt')#always use the same cid for the the password i'e uncide.txt from this repo
    cid = cid.read()
    dic = "abcdefghijklmnopqrstuvwxyz 1234567890.,"
    return stringencrypt(Message, password, dic, cid)
def decrypt(cryptedmessage, password):
    cid = open("unicode.txt",'rt')#always use the same cid for the the password i'e uncide.txt from this repo
    cid = cid.read()
    dic = "abcdefghijklmnopqrstuvwxyz 1234567890.,"
    return stringdecrypt(cryptedmessage, password, dic, cid)