player1=input("Enter first player's name: ")
player2=input("Enter second player's name: ")

while True:
    Board=["  "  for i in range(9)]
    def show_board():
        row1="| {} | {} | {} |".format(Board[0],Board[1],Board[2])
        row2="| {} | {} | {} |".format(Board[3],Board[4],Board[5])
        row3="| {} | {} | {} |".format(Board[6],Board[7],Board[8])

        print()
        print("   ",end=" ")
        print(row1)
        print("   ",end=" ")
        print(row2)
        print("   ",end=" ")
        print(row3)
        print()

    def move(icon):
        if icon=="X":
            print()
            print("Your move {}".format(player1))
            choice = int(input("Enter your choice(1-9): ").strip())
            if Board[choice-1] == "  ":
                Board[choice-1] = "X"
            else:
                print()
                print("the space is occupied!")
                move("X")

        elif icon=="O":
            print()
            print("Your move {}".format(player2))
            choice = int(input("Enter your choice(1-9): ").strip())
            if Board[choice-1] == "  ":
                Board[choice-1] = "O"
            else:
                print()
                print("the space is occupied!")
                move("O")
                
    def is_victory(icon):
        if (Board[0]==icon and Board[1]==icon and Board[2]==icon)or \
           (Board[3]==icon and Board[4]==icon and Board[5]==icon)or \
           (Board[6]==icon and Board[7]==icon and Board[8]==icon)or \
           (Board[0]==icon and Board[3]==icon and Board[6]==icon)or \
           (Board[1]==icon and Board[4]==icon and Board[7]==icon)or \
           (Board[2]==icon and Board[5]==icon and Board[8]==icon)or \
           (Board[0]==icon and Board[4]==icon and Board[8]==icon)or \
           (Board[2]==icon and Board[4]==icon and Board[6]==icon):
            return True
        else:
            return False


    def is_draw():
        if "  " not in Board:
            return True
        else:
            return False

    show_board()
    while True:
        move("X")
        show_board()
        if is_victory("X"):
            show_board()
            print("Congratulations! {}.You won the game.".format(player1))
            break
        elif is_draw():
            print("Game is draw!")
            break
        move("O")
        show_board()
        if is_victory("O"):
            show_board()
            print("Congratulations! {}.You won the game.".format(player2))
            break
        elif is_draw():
            print("Game is draw!")
            break
    ch=input("Want to play more(y/n)?: ").strip()
    if(ch!='y' and ch!='Y'):
        break
        
