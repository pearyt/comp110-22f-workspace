"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730613916"
word = str(input("Enter a 5-character word: "))
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    quit()
search_letter = str(input("Enter a single character: "))
if len(search_letter) != 1:
    print("Error: Character must be a single character.")
    quit()
print("Searching for " + search_letter + " in " + word)
i = 0
if word[0] == search_letter:
    print(search_letter + " found at index 0")
    i = i + 1 
if word[1] == search_letter:
    print(search_letter + " found at index 1")
    i = i + 1 
if word[2] == search_letter:
    print(search_letter + " found at index 2")
    i = i + 1 
if word[3] == search_letter:
    print(search_letter + " found at index 3")
    i = i + 1 
if word[4] == search_letter:
    print(search_letter + " found at index 4")
    i = i + 1 
if i == 0:
    print("No instances of " + search_letter + " found in " + word)
if i == 1:
    print("1 instance of " + search_letter + " found in " + word)
else:
    print(str(i) + " instances of " + search_letter + " found in " + word)

    

    



    
