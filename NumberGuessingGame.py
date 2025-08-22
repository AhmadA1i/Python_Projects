import random # random library to generate random number

print("Welcome to the Number Guessing Game!\nRules of the game:\n1) Give the range of numbers in which you want to guess the number\n2) Tell chances in which you will guess the number\n")

lower_bound = int(input("Enter lower bound number for this game: "))
upper_bound = int(input("Enter uppoer bound number for this game: "))

random_number = random.randint(lower_bound, upper_bound)

guess_chances = int(input("Enter the number of chances of guess: "))
guess_counter = 0

while guess_counter < guess_chances:
    user_guess = int(input("Enter your guess number: "))
    guess_counter += 1

    if user_guess == random_number:
        print(f"Hurrah! You guess the number {random_number} in {guess_counter} attempts.\n")
        break
    
    elif guess_counter >= guess_chances and user_guess != random_number:
        print("You Failed to find the number. Better Luck Next Time!\n")
        break
    
    elif user_guess > random_number:
        print("Your guess is very high\n")
    
    elif user_guess < random_number:
        print("Your guess is very low!\n" )

    