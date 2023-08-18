import random

print("Welcome to Hangman challenge")

words = ["hacker" , "bounty" , "random"]
# create an empty list
# for each letter in the secret_word and a "_" that will be
# Example if the word is hacker "_" , "_" , "_" , "_" , "_" , "_"

secret_word = random.choice(words)
print(secret_word)

display_word = ["_" for _ in secret_word]
print(display_word)

# 1 use a while loop so your game keeps going
# until the word has been guessed

game_over = False
while not game_over:
 guess = input("Guess the letter\n").lower()

# Loop through each of the letters in the chosen word
# if the letter is in the word replace the "_" with the letter
# if should look like this "_" , "a" , "_" , "_" , "_" , "_"

 for position in range(len(secret_word)):
   letter = secret_word[position]
   if letter == guess:
      display_word[position] = letter
      
 print(display_word) 

 if  "_" not in display_word:
   print("\n***YOU WIN***")
   game_over = True