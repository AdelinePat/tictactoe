import random

# Ask player to choose their sign. 
def choose_sign():
    sign1 = input("X ou O : ")
    if sign1=="X" or sign1=="x":
        sign2 = "O"
    elif sign1=="O" or sign1=="o":
        sign2 = "X"
    else:
        print("Veuillez choisir entre les deux signes proposés : X ou O. ")
        return choose_sign()
    return sign1, sign2

# Ask the player if they want to play against another player or against the bot.
def choose_opponent():
    print("Veuillez choisir votre mode de jeu :")
    print("Contre un autre joueur, entrez 1. ")
    print("Contre l'ordinateur, entrez 2. ")
    opponent = input("1 ou 2 : ")
    if opponent == "1" or opponent == "2":
        return opponent
    else:
        return choose_opponent()

# Ask a player a box to play and map the index inside coordonate.
def choose_box():
    box = input("choisir la case : ")
    
    coordonate = {
        "row": 0,
        "column":0
        }
    
    match box:
        case "A1" | "1A" | "a1" | "1a":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 1
        case "A2" | "2A" | "a2" | "2a":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 1
        case "A3" | "3A" | "a3" | "3a":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 1
        case "B1" | "1B" | "b1"  | "1b":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 2
        case "B2" | "2B" | "b2" | "2b":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 2
        case "B3" | "3B" | "b3" | "3b":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 2
        case "C1" | "1C" | "c1" | "1c":
            box_choice_ok = True
            coordonate["row"] = 1
            coordonate["column"] = 3
        case "C2" | "2C" | "c2" | "2c":
            box_choice_ok = True
            coordonate["row"] = 2
            coordonate["column"] = 3
        case "C3" | "3C" | "c3" | "3c":
            box_choice_ok = True
            coordonate["row"] = 3
            coordonate["column"] = 3
        case _:
            print("Les coordonnées ne sont pas bonnes, veuillez les entrer à nouveau.")
            box_choice_ok = False
            while box_choice_ok == False:
                return choose_box()
    return coordonate

# Check if the box is empty using the coordonate from choose_box function.
def is_box_empty(board, coordonate):
    if board[coordonate["row"]][coordonate["column"]] == " ":
        return True
    else:
        return False

# Check if all the box in the board are full or not. Return true or false.
def board_full(board,sign1,sign2):
    full = True
    line=1
    while line < 4 and full == True:
        column=1
        while column < 4 and full == True:
            if board[line][column] == sign1 or board[line][column] == sign2:
                full = True
            else:
                full = False 
            column+=1
        line+=1 
    return full

def display_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            box = f"{board[i][j]} | "
            print(box, end="")
        print("")    
        print("--+---+---+---+")
        
        # print sur la même ligne print(item, end="")

def is_victory(sign, board):
    if board[1][1] == sign and board[1][2] == sign and board[1][3] == sign:
        winner = True
    elif board[2][1] == sign and board[2][2] == sign and board[2][3] == sign:
        winner= True
    elif board[3][1] == sign and board[3][2] == sign and board[3][3] == sign:
        winner= True
    elif board[1][1] == sign and board[2][1] == sign and board[3][1] == sign:
        winner= True
    elif board[1][2] == sign and board[2][2] == sign and board[3][2] == sign:
        winner= True
    elif board[1][3] == sign and board[2][3] == sign and board[3][3] == sign:
        winner= True
    elif board[1][1] == sign and board[2][2] == sign and board[3][3] == sign:
        winner= True
    elif board[1][3] == sign and board[2][2] == sign and board[3][1] == sign:
        winner= True
    else:
        winner=False
    return winner

# Print the sign of the payer in the box they chose.
def player_turn(board, sign):
    coordonate = choose_box()
    if is_box_empty(board,coordonate) == True:
        board[coordonate["row"]][coordonate["column"]] = sign
    else:
        print("La case est déjà remplie. Veuillez en choisir une autre. ")
        return player_turn(board, sign)

# Bot turn when playing
def bot_turn(board, sign2):
    full_bot = True
    coordonate_bot = []
    coordonate_to_add = {}
    row = 1
    while row < 4 and full_bot == True:
        column = 1
        while column < 4 and full_bot == True:
            if board[row][column] == " ":
                coordonate_to_add = {"Row" : row, "Column" : column}
                coordonate_bot.append(coordonate_to_add)
            column +=1
        row +=1
    
    bot_box = random.choice(coordonate_bot)
    board[bot_box["Row"]][bot_box["Column"]] = sign2

def main():
    board = [[" ", "A", "B", "C"], [1," "," "," "], [2," "," "," "], [3," "," ", " "]]
    opponent = choose_opponent()
    sign1, sign2 = choose_sign()
    print(f"Le joueur 1 a choisi le symbole : {sign1}")
    print(f"Le joueur 2 a récupéré par défaut le symbole : {sign2}")

    winner = False
    full = False
    while winner == False | full==False:
        print()
        print("Tour du joueur 1 : ")
        player_turn(board, sign1)
        display_board(board)
        full = board_full(board,sign1,sign2)
        winner = is_victory(sign1, board)
        who_won = f"le joueur 1 ayant le symbole {sign1}"
        if winner == False | full==False:
            print()
            print("Tour du joueur 2 : ")
            if opponent == "1":
                player_turn(board,sign2)
            else:
                bot_turn(board,sign2)
            display_board(board)
            full = board_full(board,sign1,sign2)
            winner = is_victory(sign2, board)
            if opponent == "1":
                who_won = f"le joueur 2 ayant le symbole {sign2}"
            else:
                who_won = f"Dommage, le bot ayant le symbole {sign2} a gagné ..."
        if winner == True:
            print()
            print(who_won)
        elif full == True:
            print()
            print("Match Nul")
main()