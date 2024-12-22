theBoard={'7':'','8':'','9':'',
          '4':"","5":'',"6":'',
          '1':'','2':'','3':''}
Board_key=[]
for key in theBoard:
    Board_key.append(key)
def printBoard(Board):
    print(Board['7'] +'|' + Board['8'] +'|' + Board['9'] +'|' )
    print('-+-+')
    print(Board['4'] +'|' + Board['5'] +'|' + Board['6'] +'|' )
    print('-+-+')
    print(Board['1'] +'|' + Board['2'] +'|' + Board['3'] +'|' )
    print('-+-+')
def game():
    turn = 'X'
    count =0
    for i in range(10):
        printBoard(theBoard)
        print("it's your turn,"+ turn + ".Move to which place") 
        move=input()
        if theBoard[move]== '':
            theBoard[move]=turn
            count+=1
        else:
            print("the place is already filled.\nmove to which place")
            continue
        if count>=5:
            if theBoard['7']== theBoard['8'] == theBoard['9'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif  theBoard['4']== theBoard['5'] == theBoard['6'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif  theBoard['1']== theBoard['2'] == theBoard['3'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['1']== theBoard['4'] == theBoard['7'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['2']== theBoard['5'] == theBoard['8'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['3']== theBoard['6'] == theBoard['9'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['7']== theBoard['5'] == theBoard['3'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['2']== theBoard['5'] == theBoard['8'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['3']== theBoard['6'] == theBoard['9'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['7']== theBoard['5'] == theBoard['3'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
            elif theBoard['1']== theBoard['5'] == theBoard['9'] !=' ':#
                printBoard(theBoard)
                print("\n game over \n" )
                print("****"+turn+"won.****")
                break
        if count==9:
            print("\ngame over./n")
            print("it is a tie")
        if turn == 'x':
            turn='0'
        else:
            turn='x'
    restart=input("do want to pay again(y/n)")
    if restart == "y" or restart == "y":
        for key in Board_key:
            theBoard[key]=" "
            game()
                
if __name__ == "__main__":
    game()


                           
