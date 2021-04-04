# Write a Python program to count the number of strings where the string length is 2 or
# more and the first and last character are same from a given list of strings.

def match_str(wordList):
    count =  0
    for word in wordList:
        if len(wordList) > 1 and word[0] == word[-1]:
            count += 1
    return count    

wordsList = ['abc', 'xyz', 'aba', '1221','bhgsskknb','aa']    

print(match_str(wordsList))