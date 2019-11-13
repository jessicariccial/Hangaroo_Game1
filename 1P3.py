import string
letra = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
   
    remain = []
    for r in letra:
        if r not in lettersGuessed:
            remain.append(r)
    return ''.join(remain)