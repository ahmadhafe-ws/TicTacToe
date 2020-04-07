import random



user =   [True, False , False , False , False , False , False , False , False , False]
usercount =0
computer=[True, False , False , False , False , False , False , False , False , False]
computercount=0


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def printBoard(board):
    print('------------')
    print(' '+board[1]+ ' | '+board [2]+' | '+board[3])
    print('   |   |   ')
    print(' '+board[4]+ ' | '+board [5]+' | '+board[6])
    print('   |   |   ')
    print(' '+board[7]+ ' | '+board [8]+' | '+board[9])
    print('------------')

def computerplay(user , computer , usercount): #neeed to be fix not workin fine

    list=[]

    for i in range(10):
        if (user[i]==False and computer[i]==False):
            list.append(i)
            Random = random.choice(list)
    if ( not list):
        print("GAME OVER - TEKKO")
        return False


    elif (user[Random] == False and computer[Random] == False):
        computer[Random]= True
        board[Random]='O'
        printBoard(board)


        if (whoWon(computer)== True):
            print ("O won ")
            return False
        else:
            return True
    else:
        Print("GAME OVER - TEKKO")
        return False


def isEmpty(board):
    if  board.count(' ')>1:
        return True
    else:
        return False

def whoWon(list):
    if (list[1]==True and list[2]==True and list[3]==True or
        list[4]==True and list[5]==True and list[6]==True or
        list[7]==True and list[8]==True and list[9]==True or
        list[1]==True and list[4]==True and list[7]==True or
        list[2]==True and list[5]==True and list[8]==True or
        list[3]==True and list[6]==True and list[9]==True or
        list[1]==True and list[5]==True and list[9]==True or
        list[3]==True and list[5]==True and list[7]==True ):
        return True



    else:
        return False


def Teko(user_list , computer_list):
    user_true=1
    computer_true=1
    for c in range(10):
        if (user_list[c]==True):
            user_true=user_true + 1
        if(computer_list[c]==True):
            computer_true=computer_true+1
    if (computer_true > 4 and user_true > 4 and (whoWon(user_list) == False)  and (whoWon(computer_list) == False) ):
        print ("Teko")







ans=whoWon(user)
canWeGo=isEmpty(board) #use this in the while loos
while (canWeGo):
    input_temp = input("Enter number between 1-9:")
    input_current=int(input_temp)
    if input_current > 9 or input_current <1 :
        print ("number is not valid try another")
        printBoard(board)
        continue

    if user[input_current] == False and computer[input_current] == False:
        user[input_current]=True
        board[input_current]='x'
        usercount=usercount+1
        if (whoWon(user)):
            print ("-------------------------")
            print ("x is won")
            print ("-------------------------")




            break
        if(computerplay(user , computer , usercount)==False):
            break
        else:
            continue
    elif user[input_current] == True or computer[input_current] == True :
        print ("invalid field")
        printBoard(board)
        continue

    else:
        print('invalid number try again')
        continue

printBoard(board)
