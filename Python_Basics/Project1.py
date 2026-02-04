# Snake, Water, Gun
print("\t\t\t\tSNAKE, WATER AND GUN\t\t")
print("\t\t\t   Options are Snake(S), Water(W) and Gun(G)")
choice = "Y"
def outcome(choice1, choice2):
    if(choice1 == "S" and choice2 == "W"): return choice1
    if(choice1 == "S" and choice2 == "G"): return choice2
    if(choice1 == "S" and choice2 == "S"): return "Draw"

    if(choice1 == "G" and choice2 == "S"): return choice1
    if(choice1 == "G" and choice2 == "W"): return choice2
    if(choice1 == "G" and choice2 == "G"): return "Draw"

    if(choice1 == "W" and choice2 == "G"): return choice1
    if(choice1 == "W" and choice2 == "S"): return choice2
    if(choice1 == "W" and choice2 == "W"): return "Draw"

    else: return "Invalid Choice"

while(choice != "N"):
    u1_choice = input("\t\t\t\tUSER 1: Pick your Choice: ")
    u2_choice = input("\t\t\t\tUSER 2: Pick your Choice: ")

    result = outcome(u1_choice, u2_choice)
    if(result == "Draw"):
        print("\t\t\t\t\t DRAW! NO WINNER")
    elif(result == u1_choice):
        print("\t\t\t\t\t USER 1 WINS! ")
    elif(result == u2_choice):
        print("\t\t\t\t\t USER 2 WINS! ")
    else:
        print("Invalid Choice")

    choice = input("Do you want to play Again(Y/N): ")