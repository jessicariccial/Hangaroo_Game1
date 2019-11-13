def isWordGuessed(secretWord, lettersGuessed):
    
    for r in secretWord:
        if r not in lettersGuessed:
            return False
    return True