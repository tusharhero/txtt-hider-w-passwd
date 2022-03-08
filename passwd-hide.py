#/bin/python3
#will take a  password and  a string and make the string only decodable by using the password

from txt2code import c2l
from txt2code import l2c #my previous functions which are going to be used here.

def passwdnm(password,dic):#this function will take a passwd and dictionary and convert it into a number
    l = 0#counter
    nm = 1#container
    while l < len(password):#loops until the multipliciation is complete
        nm = nm + (c2l(password[l],dic)+1)#multiplies the nuber of chracter + with the nm container
        l = l + 1#counting
    return nm

def list2string(list):#converts list into string
    strin = ''#string container
    l = 0#counter
    while l < len(list):#will loop until the word is completed
        strin = strin + str(list[l])# add lth termt to the list
        l = l + 1
    return strin

def stringencrypt(string,password,dic,cid):#this function will encrypt the text and return the encrypted text as a list.
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)#getting the passwordnumber(secret)
    cryptedstring = []#empty list as a container
    while l < len(string):#looping untill complete
        mn = c2l(string[l],dic)*nm#multiplying the character length with the passwordnumber
        cryptedstring.append(cid[mn])#adding the new number's character in the spooking dic "cid" to the list
        l = l + 1#counting
    return list2string(cryptedstring)# returns it as password list sa a stirng

#driver
#print(encrypt('h','ab',"abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba"))
cid = open("unicode.txt",'rt')
cid = cid.read()
print(stringencrypt('hello I am tushar how are you',"sussybakaz","abcdefghijklmnopqrstuvwxyz ",cid))
