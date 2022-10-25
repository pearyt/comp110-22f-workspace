"""Wordle."""
__author__ = "730613916"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
global true_word
true_word = "codes"

def contains_char(guess_word : str, key : str)-> bool:
    """This function looks for matching letters and returns true if they match."""
    assert len(key) == 1
    guess_word_index: int = 0
    contains_bool = False
    while guess_word_index < len(guess_word) and contains_bool is False:
        if guess_word[guess_word_index] is key:
            contains_bool = True               
        else: 
            guess_word_index += 1
    return contains_bool  

def emojified(guess: str, secret: str) -> str():
    """This function will create green, yellow, or white 'emojis' to signify correct of not of the word."""
    assert len(guess) == len(secret)
    secret_index = 0
    global response , emojified_input 
    emojified_input = ""
    emojified_input = guess   
    response = ""
    while secret_index < len(secret):
        if guess[secret_index] is secret[secret_index]:
            response += GREEN_BOX
            secret_index += 1
        else :
            if contains_char(secret, guess[secret_index]) is True:
                response += YELLOW_BOX
                secret_index += 1
            else : 
                response += WHITE_BOX
                secret_index += 1
    return response

def input_guess(guess_number : int) -> str():
    """To make sure the user's guess is same characters long as secret word."""
    global prompt 
    user_input = input(f"Enter a {guess_number} character word: ")
    i = 0
    prompt = user_input
    while i < 1: 
        if len(prompt) != guess_number:
            prompt = str(input(f"That wasn't {guess_number} chars! Try again: "))
        else:
            i += 1
            return prompt

def main() -> None:
    """The entry point of the program and main game loop."""
    n: int() = 1
    game_over: bool = False
    while n < 7 and game_over is False:
        print(f"=== Turn {n}/6 ===")
        print(emojified(str(input_guess(len(true_word))), true_word))
        if emojified_input == true_word:
            print(f"You won in {n}/6 turns!")
            game_over = True
        else:
            n += 1
            if n is 6:    
                print("X/6 sorry, try again tomorrow!")
            
if __name__ == "__main__":
    main()
