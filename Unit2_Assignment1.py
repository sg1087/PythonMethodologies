#Shreya Gurjar
#Unit 2 Assignment 1

#This program will loop through a range from 1 to 100 and replace multiples of 3 with 'Cow'
#multiples of 7 with 'Pie', and multiples of both 3 and 7 with 'CowPie'


#created a for loop defining each integer in the range 1-100 as num
for num in range(1,101):
    
    #write if statement that prints 'CowPie' if the number is a multiple of 3 and 7
    #this statement has to be first because otherwise the loop will have already defined those integer as either 'Cow' or 'Pie'
    #therefore they will no longer be recognized as integers if the statement is last in the loop 
    if num % 3 == 0 and num % 7 == 0:
        print('CowPie')
        
    #else if the integer is only a multiple of 3 'Cow' is printed
    elif num % 3 == 0:
        print('Cow')
        
    #else if the integer is only a multiple of 7 'Pie' is printed
    elif num % 7 == 0:
        print('Pie')
        
    #else the number is printed
    else:
        print(num)
