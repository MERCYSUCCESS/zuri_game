from random import choice

def rock_paper_scissors():
    options = ["R", "P", "S"]
    user = input("Select a letter: R - Rock, P - Paper, S - Scissors; ")
    for option in options:
        if user not in options:
            print("Error! please try again:")
            user = input("Select a letter: R - Rock, P - Paper, S - Scissors; ")
        else:
            cpu = choice(options)

    print("Player ({}) : CPU ({})".format(user, cpu))


    if (user == "R") and (cpu == "S"):
        print("Player wins!")
    if (user == "S") and (cpu == "R"):
        print("CPU wins!")
    if (user == "P") and (cpu == "R"):
        print("Player wins!")
    if (user == "R") and (cpu == "P"):
        print("CPU wins!")
    if (user == "S") and (cpu == "P"):
        print("Player wins!")
    if (user == "P") and (cpu == "S"):
        print("CPU wins!")
    elif (user == cpu):
        print("It's a tie!")
        rock_paper_scissors()

rock_paper_scissors()