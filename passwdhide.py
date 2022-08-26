#/bin/python3
#will take a  password and  a string and make the string only decodable by using the password

from txt2code import c2l
from txt2code import l2c #my previous functions which are going to be used here.

def passwdnm(password,dic):#this function will take a passwd and dictionary and convert it into a number
    l = 0#counter
    nm = 1#container
    while l < len(password):#loops until the addition is complete
        nm = nm + (c2l(password[l],dic)+1)#the nuber of chracter + with the nm container + 1
        l = l + 1#counting 
        #also outing the last character
    return [nm,c2l(password[len(password)-1],dic)]

def list2string(list):#converts list into string
    strin = ''#string container
    l = 0#counter
    while l < len(list):#will loop until the word is completed
        strin = strin + str(list[l])# add lth termt to the list
        l = l + 1
    return strin

def stringencrypt(string,password,dic,cid):#this function will encrypt the text and return the encrypted text as a list.
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)[0]#getting the passwordnumber(secret)
    nml = passwdnm(password, dic)[len(passwdnm(password, dic))-1]#getting the last letter number in the password 
    cryptedstring = []#empty list as a container
    while l < len(string):#looping untill complete
        mn = c2l(string[l],dic)*nm + nml #multiplying the character length with the passwordnumber and adding the last character number
        cryptedstring.append(cid[mn])#adding the new number's character in the spooking dic "cid" to the list
        l = l + 1#counting
    return list2string(cryptedstring)# returns it as password list sa a stirng

def stringdecrypt(cryptedstring,password,dic,cid):
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)[0]#getting the passwordnumber(secret)
    nml = passwdnm(password, dic)[len(passwdnm(password, dic))-1]#getting the last letter number in the password 
    decryptedstring = []#empty list for carrying the decrypted
    while l < len(cryptedstring):#will loop until the every character is decoded
        mn = (c2l(cryptedstring[l],cid) - nml)/nm#reversing the process which was in stringcrypt()
        mn = int(mn)#converting to int
        decryptedstring.append(dic[mn])#adding the mnth character from the list to the list
        l = l + 1#counting
    return list2string(decryptedstring)
