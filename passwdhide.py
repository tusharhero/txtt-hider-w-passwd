#/bin/python3
#will take a  password and  a string and make the string only decodable by using the password
def passwdnm(password,dic):#this function will take a passwd and dictionary and convert it into a number
    nm = 1
    for char in password:
        nm += dic.index(char)+1 #the nuber of chracter + with the nm container + 1
    return [nm,dic.index(password[-1])]

def stringencrypt(string,password,dic,cid):#this function will encrypt the text and return the encrypted text as a list.
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)[0]#getting the passwordnumber(secret)
    nml = passwdnm(password, dic)[len(passwdnm(password, dic))-1]#getting the last letter number in the password 
    cryptedstring = []#empty list as a container
    while l < len(string):#looping untill complete
        mn = dic.string[l]*nm + nml #multiplying the character length with the passwordnumber and adding the last character number
        cryptedstring.append(cid[mn])#adding the new number's character in the spooking dic "cid" to the list
        l = l + 1#counting
    return string(cryptedstring)# returns it as password list sa a stirng

def stringdecrypt(cryptedstring,password,dic,cid):
    l = 0#good 'ol counter
    nm = passwdnm(password, dic)[0]#getting the passwordnumber(secret)
    nml = passwdnm(password, dic)[len(passwdnm(password, dic))-1]#getting the last letter number in the password 
    decryptedstring = []#empty list for carrying the decrypted
    while l < len(cryptedstring):#will loop until the every character is decoded
        mn = (cid.cryptedstring[l] - nml)/nm#reversing the process which was in stringcrypt()
        mn = int(mn)#converting to int
        decryptedstring.append(dic[mn])#adding the mnth character from the list to the list
        l = l + 1#counting
    return string(decryptedstring)