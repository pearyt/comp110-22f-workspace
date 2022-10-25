"""Initialize variables."""
__author__ = "730613916"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
correct_word = "python"
index_correct_word = 0
response = ""
word = str(input(f"What is your {len(correct_word)}-letter guess? "))
i = 0
"""I have a while loop to continue over and over until it receives an input as the same number of letters as the secret word. """
while i < 1: 
    if len(word) != len(correct_word):
        word = str(input(f"That was not {len(correct_word)} letters! Try again: "))
    else:
        i += 1 
        if word != correct_word:
            print("Not quite. Play again soon!")
        else: 
            print("Woo! You got it!")
"""This is a while loop to create green squares matching the letters to the secret word."""
while index_correct_word < len(correct_word):    
    if word[index_correct_word] == correct_word[index_correct_word]:
        response = response + GREEN_BOX        
        index_correct_word += 1
    else:
        test_letter_bool = False
        alternate_indice = 0
        while alternate_indice < len(correct_word) and (test_letter_bool is False):
            if word[index_correct_word] is correct_word[alternate_indice]:                
                test_letter_bool = True
            else:
                alternate_indice += 1                   
        if test_letter_bool is True:
            response += YELLOW_BOX
            index_correct_word += 1
        else: 
            response += WHITE_BOX
            index_correct_word += 1
print(response)


     



    
