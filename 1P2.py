def getGuessedWord(secretWord, lettersGuessed):
   
    result = []
    for r in secretWord:
        if r in lettersGuessed:
            result.append(r)
        else:
            result.append('_')
    return ' '.join(result)