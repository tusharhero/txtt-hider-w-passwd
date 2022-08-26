def getoccurrences(l):
    occur = {}
    oc = list(set(list(l)))
    for a in oc:
        length = l.count(a)
        occur[a] = length
    print(occur)
    return occur

def getdistri(dic):
    return {key: val for key, val in sorted(dic.items(),reverse=True, key = lambda ele: ele[1])}

def getletters(dic,let_freq):
    dic = list(dic.keys())
    letters = {}
    for n in range(len(dic)):
        letters[dic[n]] = let_freq[n]
    return letters

let_freq = [" ","e","a","r","i","o","t","n","s","l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]

def decrypt(encryptedmessage, letters):
    decryptedmessage = ""
    for n in encryptedmessage:
        decryptedmessage += letters[n]
    return decryptedmessage


def heckthemessage(message, let_freq = ["e","a","r","i","o","t","n","s","l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]):
    occur = getoccurrences(message)
    distri  = getdistri(occur)
    letters = getletters(distri,let_freq)
    return decrypt(message, letters)

print(heckthemessage(input("Enter the text(big messages work best) : ")))