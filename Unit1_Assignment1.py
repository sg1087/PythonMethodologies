#Shreya Gurjar
#Assignment 1
    #Create a program that will take a user input number of inches
    #and convert it to output feet, yards, and miles



#initialize inches with a user input using the input function
#cast the user input as an integer 
inches = int(input('Please enter the number of inches: '))

#convert the inches to feet by dividing by 12 
feet = inches/12

#convert the feet to yards by dividing by 3 
yards = feet/3

#convert the yards to miles by dividing by 1760
miles = yards/1760

#print all of the results after casting the variables to string
print(str(feet) + ' feet')
print(str(yards) + ' yards')
print(str(miles) + ' miles')

