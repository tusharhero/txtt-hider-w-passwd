#/bin/python3
#will take a  password and  a string and make the string only decodable by using the password

def c2l(s,dic):#this function will figure out the placement in dictionary
    l = 0#variable will contain the placment in dictionary
    while l < len(dic): #will break if l is more than the length of dictionary
        if s == dic[l]:# if it finds the s is equal to the current character in the dictionary it returns it
            return l
        else:#if it is not the case it just adds 1 to it and loops again
            l = l + 1
    return int(l/2) #if not found at all returns this

def l2c(s,dic,cid):#this function will convert the character's position into letter
    l = c2l(s,dic)#uses the c2l() to get the position
    c = cid[l]#return the character
    return c

'''
def passwdnm(password,dic):#this function will take a passwd and dictionary and convert it into a number and another number
    l = 0#counter
    nm = 1#container
    while l < len(password):#loops until the multipliciation is complete
        nm = (c2l(password[l],dic)+1) * nm#multiplies the nuber of chracter + with the nm container
        l = l + 1#counting
    nm = nm + (c2l(password[l-1],dic))#just a last operation
    print(nm)
    return nm
#'''
#'''
def passwdnm(password,dic):#this function will take a passwd and dictionary and convert it into a number
    l = 0#counter
    nm = 1#container
    while l < len(password):#loops until the multipliciation is complete
        nm = (c2l(password[l],dic)+1) + nm#multiplies the nuber of chracter + with the nm container
        l = l + 1#counting
    print(nm)
    return nm

def list2string(list):#converts list into string
    strin = ''#string container
    l = 0#counter
    while l < len(list):#will loop until the word is completed
        strin = strin + str(list[l])# add lth termt to the list
        l = l + 1
    return strin
#'''
def stringencrypt(string,password,dic,cid):#this function will encrypt the text and return the encrypted text as a list.
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)#getting the passwordnumber(secret)
    cryptedstring = []#empty list as a container
    while l < len(string):#looping untill complete
        mn = c2l(string[l],dic)*nm#multiplying the character length with the passwordnumber
        cryptedstring.append(cid[mn])#adding the new number's character in the spooking dic "cid" to the list
        l = l + 1#counting
    return list2string(cryptedstring)# returns it as password list sa a stirng

'''
def encrypt(string,password,dic,cid):
    len(password)
    l = 1
    while 
    passs = (c2l(password[0], dic)+1) * (c2l(password[1], dic)+1)
    place = string[0]*passs
    return l2c(1, dic, cid)
'''

#driver
#print(encrypt('h','ab',"abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba"))
cid = open("unicode.txt",'rt')
cid = cid.read()
print(stringencrypt('hello I am tushar how are you',"sussybakaz","abcdefghijklmnopqrstuvwxyz ",cid))
