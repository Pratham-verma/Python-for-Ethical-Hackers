# Hello everyone! , we are learning how to implement a 'Nested if statements statements' in python

# A nested if statement used to create a more complex decision-making structure within a program.
# It involves using one if statement inside another if statement.

Score = input("What is your score?\n")
Score = int(Score)

if Score >= 90:
   age =  int(input("what is your age?\n"))
   if age < 15:
      print("That's great your grade is A+")
   else:
    print("your grade is A")

if Score >= 80:
   age =   input("what is your age?\n")
   if age < 15:
       print("That's great your grade is B+")
   else:
        print("your grade is B")
   

if Score >= 70:
    print("your grade is C")
else:
      print("Next time study more")
    
  

      
