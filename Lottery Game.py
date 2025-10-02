import random

def lottery_game():

    lottery_number = random.randint(100, 999)

    print("Welcome to the Lottery Game!")
    guess = int(input("Enter your 3-digit guess: "))

    print(f"\nLottery Number: {lottery_number}")
    print(f"Your Guess: {guess}")

    if guess == lottery_number:
        print(" Exact match! You win ₱10,000!")
    elif sorted(str(guess)) == sorted(str(lottery_number)):
        print("All digits match! You win ₱5,000!")
    elif any(d in str(lottery_number) for d in str(guess)):
        print("One digit matches! You win ₱1,000!")
    else:
        print("Sorry, no match. Better luck next time!")


lottery_game()