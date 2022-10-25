"""Create your own adventure: Coinflipping game to guess how many correct in a row."""
import random
__author__: str = "730613916"

points: int = 0
player: str = ""
NAMED_CONSTANT: str = "\U0001F601"
sad_face: str = "\U0001F62D"
emoji_counter: int = 0
i: int = 0
action: int = 0
rand_num: int = 0


def main() -> None:
    """The general body of the code."""
    global player, points, NAMED_CONSTANT, sad_face, emoji_counter, i, rand_num, action
    greet()
    while i < 1:
        menu()
        player_menu(action)
        
        
def greet() -> None:
    """A greeting function to welcome the player."""
    print(f"\nWelcome to the coin flipping game!\n{NAMED_CONSTANT}\nWhat is your name?")
    global emoji_counter, player, points
    emoji_counter += 1
    print("What is your name?")
    player = str(input())
    
    
def menu() -> None:
    """Give the player a menu on what actions to take."""
    print(f"\nHello {player}, what would you like to do?\n1.Check out Rules\n2.Spin\n3.Check Points\n4.Quit")
    global action
    action = int(input("Which number option do you choose? "))
    

def player_menu(player_int: int) -> None: 
    """Based on the integer that the player inputs, certain actions will be performed."""
    global rand_num, i
    if player_int == 1:
        print("\nRules: Guess 0 for Heads, or 1 for Tails for a coin flip. If you guess correctly, you gain points. If you are wrong, Game Over.")
    elif player_int == 2:
        rand_num = random.randint(0, 1)
        guess_coin(rand_num)
    elif player_int == 3:
        print(f"\n{player}, you have {points} points")
    elif player_int == 4:
        i += 2
        print(f"Farewell {player}, you had {points} points. \n{emoji_counter} emoji's were printed.")
        quit()
    else:
        print("Enter a number option from the list: 1, 2, 3, or 4")


def guess_coin(rand_num: int) -> None:
    """A function to define what will happen when you guess what side the coin lands on."""
    player_decision: int = int(input("What side will the coin land on? "))
    if player_decision == 0 or player_decision == 1:
        global points, i, emoji_counter
        if player_decision == rand_num and rand_num == 0:
            emoji_counter += 1
            points += 1
            print(f"You got it right! {NAMED_CONSTANT}\nThe Answer was Heads. \nPoints increase by one!")
        elif player_decision == rand_num and rand_num == 1:
            emoji_counter += 1
            points += 1
            print(f"You got it right! {NAMED_CONSTANT}\nThe Answer was Tails. \nPoints increase by one!")
        elif player_decision != rand_num and rand_num == 0:
            emoji_counter += 1
            print(f"You got it wrong. {sad_face}\nThe Answer was Heads\nGame Over \n{player} had {points} points \n{emoji_counter} emoji's were used.")
            i += 2
            quit()
        else: 
            emoji_counter += 1
            print(f"You got it wrong. {sad_face}\nGame Over \n{player} had {points} points \n{emoji_counter} emoji's were used.")
            i += 2
            quit()
    else:
        print("\nEnter either 0 for heads or 1 for tails")
   

if __name__ == "__main__":
    main()