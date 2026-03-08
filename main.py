import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")
def start_game():
    random_number = int(random.randint(1, 11))
    print("Hey there! Welcome to the Number Guessing Game!")
    player_name = input("Enter your name: ")
    wanna_play = input(f"Hi {player_name}! Would you like to play the game? (Enter Yes/No): ")
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 to 11: "))
            if int(guess) < 1 or int(guess) > 11:
                raise ValueError("Please guess a number within a given range.")
            if int(guess) == random_number:
                print("Congrats! You guessed it right!")
                attempts += 1
                attempts_list.append(attempts)
                print(f"It took you {attempts} attempts.")
                play_again = input("Would you like to play again? (Enter Yes/No): ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 11))
                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
            elif int(guess) > random_number:
                print("It's Lower.")
                attempts += 1
            elif int(guess) < random_number:
                print("It's Higher.")
                attempts += 1
        except ValueError as err:
            print(f"{err}")
    else:
        print("That's cool, have a nice day!")
if __name__ == '__main__':
    start_game()