import random
strchoose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
choose = int(strchoose)
if choose >= 3 or choose < 0:
    print("Invalid number you lose")
else:
    rock = """
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """
    paper = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
    scissors = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """
    game = [rock, paper, scissors]
    print("Your choose:")
    print(game[choose])
    computer_choose = random.randint(0, 2)
    print("Computer choose:")
    print(game[computer_choose])
    if choose == computer_choose:
        print("It's a draw")
    elif choose == 0:
        if computer_choose == 1:
            print("You lose")
        else:
            print("You win")
    elif choose == 1:
        if computer_choose == 0:
            print("You win")
        else:
            print("You lose")
    else:
        if computer_choose == 0:
            print("You lose")
        else:
            print("You win")
