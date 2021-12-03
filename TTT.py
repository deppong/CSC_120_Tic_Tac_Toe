# Isaiah Deppong
#

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    
rows = len(board)
cols = len(board[0])
turn = 0


def printboard():
    for i in range(0, 9, 3):
        print(f'{board[i]}, {board[i+1]}, {board[i+2]}')


def whosturn():
    if turn % 2 == 0:
        return 0
    else:
        return 1


def taketurn():
    while True:
        try:
            position = int(input("Enter move (0-8): "))
            if board[position] == '-':
                if whosturn() == 0:
                    board[position] = 'X'
                else:
                    board[position] = 'O'
                break
            else:
                print("Spot already taken!")
        except:
            print("Please enter valid move")




printboard()
taketurn()
turn += 1
printboard()
taketurn()
turn += 1
printboard()
