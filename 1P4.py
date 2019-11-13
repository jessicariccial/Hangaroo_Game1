def Hangaroo(secretWord):
    
    print('WELCOME TO HANGAROO!')
    print('I know a word that is', len(secretWord), "letters long. Can you find out what is it?")
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Go, guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Great work:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Oh no! That letter is not in the word:", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print('GAME OVER. The word was', secretWord)
        	break
        else:
        	continue
