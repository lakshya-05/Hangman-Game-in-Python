# Hangman-Game-in-Python
Created a simple game using basic concepts of python language.

## Logic used : 
Create a list of words you want to select for the game.
Move all the gussed letters by the user into a set to avoid any repeatition of letters.

### Cases:
  if user repeated a guess, then ask for another letter.
  if user guessed the correct letter from the word - add the letter to the set.
  else the guessed letter is not in the word, so reduce 1 from the given attempts from the user(I've provided 6 attempts) 

if attempts is equal to zero then the game is over.
else, user guessed the whole word correctly then end the game by exiting the while loop.
