import random
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != number:
        print("You didnt guess it, try again.")
    else:
        print("Congratulations! You guessed the number, want to play again?")
        play_again = input("Type 'yes' to play again or 'no' to exit: ")
        while play_again.lower() == 'yes':
            number = random.randint(1, 10)
            guess = 0
            while guess != number:
                guess = int(input("Guess a number between 1 and 10: "))
                if guess != number:
                    print("You didnt guess it, try again.")
                else:
                    print("Congratulations! You guessed the number, want to play again?")
                    play_again = input("Type 'yes' to play again or 'no' to exit: ")
            if play_again.lower() == 'no':
                print("Thanks for playing! Goodbye!")
                break        
