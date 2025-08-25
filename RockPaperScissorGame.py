import random

print("""Welcom to the rock paper scissor game!
      \n Rules of Game:
       \n1- user will select 1 for rock 2 for paper and 3 for scissor 
       \n2- first turn human second turn computer 
       \n3- Rock Paper -> Paper\nRock Scissor -> Rock\n Scissor Paper -> Scissor\n""")

while True:


    print("user's turn!\n")
    choice_num = int(input("Enter a number of choice: "))
    while (choice_num < 1 or choice_num > 3):
        choice_num = int(input("Please Enter a number between 1 and 3: "))

    if choice_num == 1:
        choice_name = 'Rock'
    elif choice_num == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("User's choice: ", choice_name)
    print("Now computers turn!\n")

    comp_choice_num = random.randint(1,3)
    if comp_choice_num == 1:
        comp_choice_name = 'Rock'
    elif comp_choice_num == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("computer's choice: ", comp_choice_name)
    print(choice_name, " vs ", comp_choice_name)

    if choice_name == comp_choice_name:
        result = 'Draw'
    elif (choice_num == 1 and comp_choice_num == 2) or (choice_num == 2 and comp_choice_num == 1):
        result = 'Paper'
    elif (choice_num == 1 and comp_choice_num == 3) or (choice_num == 3 and comp_choice_num == 1):
        result = 'Rock'
    elif (choice_num == 2 and comp_choice_num == 3) or (choice_num == 3 and comp_choice_num == 2):
        result = 'Scissor' 

    if choice_name == result:
        print("user wins")
    elif comp_choice_name == result:
        print("computer wins")
    else:
        print("Draw")

    ch = input("Do you want to play again (Y/N): ")
    if ch.lower() == 'n':
        break

print("Thanks for playing!\n")




