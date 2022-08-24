"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = '73063916'

word = str(input("Enter a 5-character word: "))
search_letter = str(input("Enter a single character: "))
print("Searching for " + search_letter + " in " + word)
word = 'hello'

i = 0
if word[0] == search_letter:
    print(search_letter + " found at index 1")
    i = i+1 
if word[1] == search_letter:
    print(search_letter + " found at index 2")
    i = i+1 
if word[2] == search_letter:
    print(search_letter + " found at index 3")
    i = i+1 
if word[3] == search_letter:
    print(search_letter + " found at index 4")
    i = i+1 
if word[4] == search_letter:
    print(search_letter + " found at index 5")
    i = i+1 

if i == 0:
    i = 'No '
print(i + " instances of " + search_letter + " found in " + word)

    

    



    
