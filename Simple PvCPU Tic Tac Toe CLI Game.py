from random import choice
def AddLetter(letter,postion):
    board[postion] = letter

def CheckFree(postion):
    return board[postion] == ' '      

def PrintBoard(board):
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')

def CheckWinner(board,letter):
    return((board[1] == board[2] == board[3] == letter) 
    or (board[4] == board[5] == board[6] == letter)
    or (board[7] == board[8] == board[9] == letter)
    or (board[1] == board[4] == board[7] == letter)
    or (board[2] == board[5] == board[8] == letter)
    or (board[3] == board[6] == board[9] == letter)
    or (board[1] == board[5] == board[9] == letter)
    or (board[3] == board[5] == board[7] == letter))

def CheckBoardFull(board):
    return board.count(' ') == 1 

def HumanMove(board):
    while True :
        postion = input("Selecte the postion you want to place an 'X' in (1-9): ")
        try :
            postion = int(postion)
            if postion >= 1 and postion <=9 :
                if CheckFree(postion):
                    AddLetter("X",postion)
                    break
                else :
                    print("Sorry, the postion is aleardy used :3")
            else :
                print("Please, Select a postion with the range -_-")
        except:
            print(" Please, enter a vaild postion -_-")
            
def AiMove(board):   
    freepostions= [x for x , letter in enumerate(board) if letter == ' ' and x != 0]
    
    if not(freepostions):
        return 0
    for letter in ["O","X"] :
        for postion in freepostions :
            boardcopy = board[:]
            boardcopy[postion]= letter
            if CheckWinner(boardcopy,letter):
                AddLetter("O",postion)
                return postion
    
    freecorners =[]
    for i in [1,3,7,9]:
        if i in freepostions :
            freecorners.append(i)
    if freecorners :
        postion = choice(freecorners)
        AddLetter("O",postion)
        return postion
    
    if 5 in freepostions:
        AddLetter("O",5)
        return 5
    postion = choice(freepostions)
    AddLetter("O",postion)
    return  postion
            
def main():
    print("Welcome! Try win me in X-O, I'll let you start !" )
    print("Let's GO!!!")
    while True :
        if CheckBoardFull(board) :
            print("Meh, It's a tie :3 ")
            break

        HumanMove(board)
        PrintBoard(board)         
        
        if CheckWinner(board,'X'):
            print("Meh, You won :( , I'll take my revange later :* ")
            break
        
        aimv = AiMove(board)
        if aimv == 0 :
            print("Meh, It's a tie :3 ")
            break
        else :
            print (" I put 'O' in postion " , aimv) 
            PrintBoard(board)

        if CheckWinner(board,'O'):
            print("I won!! Good luck next time!")
            break

    
while True :
    board = [' ' for i in range(10)]
    main()
    while True :
        i=  input("Type 1 to play again , 2 to terminate ")
        if i == "1" :
            breaker = False
            break
        elif i == "2":
                breaker= True
                break
        else :
            print(" Please, enter 1 or 2  -_-")
    if breaker:
        break