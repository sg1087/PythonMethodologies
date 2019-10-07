#Shreya Gurjar
#Unit 2 Assignment 2

#This program will print out the average of the negative numbers in the list
#that appear before a 999 is detected in MyList 

MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]

#create an empty list 
negative_num = []

#for loop through MyList defining each integer as num
for num in MyList:

    #if num is the number 999 break the loop so it does not go past 999
    if num == 999:
        break

    #else all the negative numbers are appended to the negative_num list 
    elif num < 0:
        negative_num.append(num)
        
#make a counter for the new loop
negative_sum = 0

#for loop through the intergers in the negative_num list 
for i in negative_num:

    #add each iteration to the negative_sum counter
    negative_sum = negative_sum + i
    
#take the average by dividing the sum of the negative numbers by the length of the negative_num list 
MyList_avg = (negative_sum)/len(negative_num)

#print the average 
print('The average of all the negative numbers before 999 in MyList is: ' + str(MyList_avg))
