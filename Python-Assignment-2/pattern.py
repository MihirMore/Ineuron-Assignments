## Create the below pattern using nested for loop in Python.
'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
for rows in range(0 , 5):
    for columns in range( 0 , rows + 1):
        print("*",end="")
    print()  
for row in range (5 , 0 , -1):
    for column in range(0 , row - 1):
        print("*",end="")
    print() 

