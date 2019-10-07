#Shreya Gurjar
#Assignment 2
    #Create a program in Python that stores an age
    #and a weight (just set up two hard coded variables)
    #and allow the user to try to guess your two numbers.


#initialize the age and weight variables with two integers 
age = 25
weight = 135

#initialize the user input as integers in the age_guess and weight_guess variables
age_guess = int(input('Enter your guess for age: '))
weight_guess = int(input('Enter your guess for weight: '))

#if statement to print 'Both Higher' if the guesses are both higher than the original
if (age_guess > age) and (weight_guess > weight):
    print('Both Higher')

#else if print 'Both Lower' if the guesses are both lower than the original     
elif (age_guess < age) and (weight_guess < weight):
    print('Both Lower')

#else if print 'Bingo' if the guesses are both exact to the original 
elif (age_guess == age) and (weight_guess == weight):
    print('Bingo')

#else print 'Game Over' when none of the previous conditions are satisfied 
else:
    print('Game Over')
