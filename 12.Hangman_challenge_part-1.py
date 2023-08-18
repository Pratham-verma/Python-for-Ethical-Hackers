import random

# create a greeting.
print("Welcome to Hangman challenge\n")

# create your word list.
words = ["hacker","bounty","random"]

# randomly choose a word form the list you have created.
secret_word = random.choice(words)

# ask the user to guess a letter.
guess = input("Guess a letter ").lower()
print(guess)

# bonus make teh program take the input from the user and make it lowercase.
# check if the letter is in the word.
for letter in secret_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    

