# Isaiah Deppong
# Edward Kusa
# 12/2/2021

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    

def printboard():
    for i in range(0, 9, 3):
        print(f'{board[i]}, {board[i+1]}, {board[i+2]}')


def whosturn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'


def taketurn(turn):
    while True:
        try:
            position = int(input("Enter move (0-8): "))
            if board[position] != 'O' or board[position] != 'X':
                board[position] = whosturn(turn)
                break
            else:
                print("Spot already taken!")
        except:
            print("Please enter valid move")

def checkwin():
    if board[0] == board[1] == board[2]: return True
    elif board[3] == board[4] == board[5]: return True
    elif board[6] == board[7] == board[8]: return True
    elif board[0] == board[3] == board[6]: return True
    elif board[1] == board[4] == board[7]: return True
    elif board[2] == board[5] == board[8]: return True
    elif board[0] == board[4] == board[8]: return True
    elif board[2] == board[4] == board[6]: return True
    else: return False


def main():
    turn = 0

    while turn < 9:
        printboard()
        taketurn(turn)
        if checkwin():
            printboard() 
            print(f'{whosturn(turn)} Won!')
            break
        turn += 1

    if not checkwin():
        printboard()
        print('Game is a tie') 


main()