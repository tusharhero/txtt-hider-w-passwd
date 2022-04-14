'''
WRITTEN by Tushar Maharana
LICENSE: https://tusharhero.mit-license.org/

“Code” Generator
Will take text and convert it into code (replace the letters)
'''
def c2l(s,dic):#this function will figure out the placement in dictionary
    l = 0#variable will contain the placment in dictionary
    while l < len(dic): #will break if l is more than the length of dictionary
        if s == dic[l]:# if it finds the s is equal to the current character in the dictionary it returns it
            return l
        else:#if it is not the case it just adds 1 to it and loops again
            l = l + 1
    return 0 #if not found at all returns this

def l2c(s,dic,cid):#this function will convert the character's position into letter
    l = c2l(s,dic)#uses the c2l() to get the position
    c = cid[l]#return the character
    return c

def txt2code(txt,dic,cid): #now using the functions to convert string to gnirts
    l = 0
    sussy = '' #string container 
    while l < len(txt):#will finish after the length is finished
        sussy = sussy + l2c(txt[l], dic, cid)#add the lth character to the string
        l = l + 1#counting
    return sussy
'''
#driver
ss = input()
ab = 'abcdefghijklmnopqrstuvwxyz '
ba = 'zyxwvutsrqponmlkjihgfedcba '
x = txt2code(ss,ab,ba)
print(x)
x = txt2code(x,ba,ab)#to convert back to text just reverse the string
print(x)
'''