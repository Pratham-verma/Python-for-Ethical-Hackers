# Hello everyone! , we are learning how to make a 'Functions' in python

# A function in Python is like a reusable recipe for performing a specific task.
# few steps to write function :-
# 1. Define: Start by using the def keyword, followed by the name you want to give your function.
# 2. Code: Write the code you want your function to execute. This is the block of code that will run whenever you call the function.
# 3. Return (Optional): If your function should provide some result or output.


choice = int(input("What would you like to choice?\n"))

def function(choice):
 for num in range(0,choice):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")    
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz") 
    else:
        print(num)       

function(choice)