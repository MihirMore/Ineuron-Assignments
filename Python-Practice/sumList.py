#Write a Python program to sum all the items in a list.

def sumList(numList):
    sum_number = 0
    for i in numList:
        sum_number += i 
    return sum_number

print(sumList([23,43,56,-76,32,-27,43,-11]))
