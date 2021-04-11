import random

boardWith = 11
boardHeight = 11
SymbolEmpty=' '
SymbolBase='X'
SymbolPath='O'
SymbolExitTile ='H'
SymbolEntryStrip= 'J'
ListOfPlayers = []
Pawn1='1'
Pawn2='2'
Pawn3='3'
Pawn4='4'
Pawn5='5'
Pawn6='6'
Pawn7='7'
Pawn8='8'

teamTurn = 1

class Player:
    def __init__(self, col, num, pos):
        self.color = col
        self.alive = 1
        self.safe = 1
        self.number = num
        self.Lx = pos
        self.looped = 0
        
        
    def update(mover):
        pos = pos+mover

def gameInit ():
    
    for i in range(2): #Number of teams
        for j in range(4): #Number of players per team
            if i == 1:
                Color = 0
            else:
                Color = 1
            player = Player(Color, j, -1)
            ListOfPlayers.append(player)
    #ListOfPlayers[0].Lx = 10
    #ListOfPlayers[1].Lx = 20
    #ListOfPlayers[2].Lx = 0
    #ListOfPlayers[3].Lx = 30
    ListOfPlayers[4].Lx = 36
    ListOfPlayers[5].Lx = 37
    ListOfPlayers[6].Lx = 38
    ListOfPlayers[7].Lx = 39


    ListOfPlayers[0].color = 1
    ListOfPlayers[1].color = 1
    ListOfPlayers[2].color = 1
    ListOfPlayers[3].color = 1
    ListOfPlayers[4].color = 2
    ListOfPlayers[5].color = 2
    ListOfPlayers[6].color = 2
    ListOfPlayers[7].color = 2
    


    
    teamTurn = 1

Board = ["XX  OOH  XX",
         'XX  OJO  XX',
         '    OJO    ',
         '    OJO    ',
         'HOOOOJOOOOO',
         'OJJJJTJJJJO',
         'OOOOOJOOOOH',
         '    OJO    ',
         '    OJO    ',
         'XX  OJO  XX',
         'XX  HOO  XX']



def LxToBoardCoords (LxCoords, player):
    if LxCoords > 39 and ListOfPlayers[player].color == 2:
        LxCoords = LxCoords - 40
        ListOfPlayers[player].looped = 1
    if LxCoords < 5:
        return(4,10-LxCoords)
    if LxCoords < 9 and LxCoords >= 5:
        return (10-LxCoords-1, 6)
    if LxCoords == 9:
        return(0,5)
    if LxCoords > 9 and LxCoords < 15:
        return(LxCoords-10, 4)
    if LxCoords >= 15 and LxCoords < 19:
        return(4,3-(LxCoords-15))
    if LxCoords == 19:
        return(5,0)
    if LxCoords >= 20 and LxCoords < 25:
        return(6, LxCoords-20)
    if LxCoords >= 25 and LxCoords < 29:
        return(6+LxCoords-24 , 4)
    if LxCoords == 29:
        return(10,5)
    if LxCoords > 29 and LxCoords < 35:
        return(10-(LxCoords-30) , 6)
    if LxCoords >= 35 and LxCoords < 39:
        return(6, (10-3)+(LxCoords-35))
    if LxCoords == 39:
        return(5,10)
    raise Exception(f'Unknown lxcoords {LxCoords}')
            
        
    
    
def drawBoard ():
    printedPlayer = 0
    for i in range(boardHeight):
        for j in range(boardWith):
            for y in range(len(ListOfPlayers)):
                a  = [0,0]
                a = LxToBoardCoords(ListOfPlayers[y].Lx, y)
                if a[0] == j and a[1] == i and printedPlayer == 0:
                    print(y, end='')
                    printedPlayer = 1
            if printedPlayer == 0:
                print(Board[i][j], end="")
            printedPlayer = 0
        print('')
    print("---------------------------------")
    print('')
    print('')
    print('---------------------------------')
    


def handleUserInput ():
    while True == True:
        try:
            selected = int(input("Confrim moving that pawn, or pick a diffret one. If you see this message alot you are selecting an invalid pawn."))
            if teamTurn == 1 and selected < 4:
                break
            if teamTurn == 2 and selected >= 4 and selected < 8:
                break
        except:
                print('You entered an invalid input, please try again')
        print("COME ON")

def GameUpdate():
    global teamTurn
    ignorer = 0
    SpotsToMove = random.randint(1,4)
    a = input("Hit enter to throw the dice")
    print("You can move " + str(SpotsToMove) + " spots.")
    print('')


    
    for i in range(len(ListOfPlayers)):
        if ListOfPlayers[i].Lx > 39 and ListOfPlayers[i].color == 2:
            ListOfPlayers[i].Lx = ListOfPlayers[i].Lx - 39
            ListOfPlayers[i].looped = 1
        if ListOfPlayers[i].Lx >= 39 and ListOfPlayers[i].color == 1:
            listOfPlayers[i].Lx = -2
        if ListOfPlayers[i].Lx > 9 and ListOfPlayers[i].color == 2 and ListOfPlayers[i].looped == 1:
            ListOfPlayers[i].Lx = -2
        if teamTurn == 1:
            if ListOfPlayers[0].Lx == -2 and ListOfPlayers[1].Lx == -2 and ListOfPlayers[2].Lx == -2 and ListOfPlayers[3].Lx == -2 :
                print("PRVI TEAM JE POBEDIO!")
                exit()
        if teamTurn == 2:
            if ListOfPlayers[4].Lx == -2 and ListOfPlayers[5].Lx == -2 and ListOfPlayers[6].Lx == -2 and ListOfPlayers[7].Lx == -2:
                print("DRUGI Team je pobedio")
                exit()
    if a == "":
        
        if ListOfPlayers[0].Lx == -1 and ListOfPlayers[1].Lx == -1 and ListOfPlayers[2].Lx == -1 and ListOfPlayers[3].Lx == -1 and teamTurn == 1 and SpotsToMove != 6:
            print("nemas pokrete, zavrsio ti se red.")
            print('')
            print('')
            print("tripped 1")
            teamTurn = 2
            return
        print(ListOfPlayers[5].Lx)
        if ListOfPlayers[4].Lx == -1 and ListOfPlayers[5].Lx == -1 and ListOfPlayers[6].Lx == -1 and ListOfPlayers[7].Lx == -1 and teamTurn == 2 and SpotsToMove != 6:
            print("nemas pokrete, zavrsio ti se red.")
            print('')
            print('')
            teamTurn = 1
            return        

        selected = -3
        handleUserInput()
        if SpotsToMove == 6:
            print("I am stuck")
            while True == True:
                try:
                    selected = int(input("Confrim moving that pawn, or pick a diffret one. If you see this message alot you are selecting an invalid pawn."))
                    if teamTurn == 1 and selected < 4:
                        break
                    if teamTurn == 2 and selected >= 4 and selected < 8:
                        break
                except:
                        print('You entered an invalid input, please try again')
                
            if ListOfPlayers[selected].Lx == -1:
                if ListOfPlayers[selected].color == 1 and ListOfPlayers[0].Lx != 0 and ListOfPlayers[5].Lx != 0 and ListOfPlayers[2].Lx != 0 and ListOfPlayers[3].Lx!= 0:
                    ListOfPlayers[selected].Lx = 0
                    ignorer = 1
                if ListOfPlayers[selected].color == 0 and ListOfPlayers[4].Lx != 10 and ListOfPlayers[5].Lx != 10 and ListOfPlayers[6].Lx != 10 and ListOfPlayers[7].Lx!= 10:
                    ListOfPlayers[selected].Lx = 10
                    ignorer = 1
                for j in range(len(ListOfPlayers)):
                    if ListOfPlayers[selected].Lx == ListOfPlayers[j].Lx:
                        ListOfPlayers[j].Lx == -1
                return
        
        print("step 1")
        # Handle user input
        handleUserInput()
        while True == True:
            try:
                selected = int(input("Confrim moving that pawn, or pick a diffret one. If you see this message alot you are selecting an invalid pawn."))
                if teamTurn == 1 and selected < 4:
                    break
                if teamTurn == 2 and selected >= 4 and selected < 8:
                    break
                giveUp = input("Write  done  to end your turn, this is used when you cant take out a pawn or move any.")
                if giveUp == "done":
                    break
            except:
                print('You entered an invalid input, please try again')
            
            
        print("Step 2")                               
        if ignorer == 0:
            if teamTurn == 1:
                while True == True:
                    
                    print('1x')
                    print("12")
                    if ListOfPlayers[selected].Lx != -1 and \
                    ListOfPlayers[0].Lx != ListOfPlayers[selected].Lx+SpotsToMove and
                    ListOfPlayers[1].Lx != ListOfPlayers[selected].Lx+SpotsToMove and
                    ListOfPlayers[2].Lx != ListOfPlayers[selected].Lx+SpotsToMove and
                    ListOfPlayers[3].Lx != ListOfPlayers[selected].Lx+SpotsToMove:
                        ListOfPlayers[selected].Lx = ListOfPlayers[selected].Lx + SpotsToMove
                        ready = ListOfPlayers[selected].Lx
                        print("im in")
                        return
                        for j in range(len(ListOfPlayers)):
                            if ListOfPlayers[selected].Lx == ListOfPlayers[j].Lx and ListOfPlayers[i].color != ListOfPlayers[j].color:
                                ListOfPlayers[j].Lx = -1
                                ListOfPlayers[selected].Lx = ready
                    else:
                        handlePlayerInput()
                teamTurn = 2

            else:
                if teamTurn == 2:
                    print('2x')
                    print(ListOfPlayers)
                    while True == True:
                        print("HI")
                        if ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[4] and
                        ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[5] and
                        ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[6] and
                        ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[7]:
                            print("2")
                            break
                        else:
                            print("3")
                            handlePlayerInput()
                    
                    ListOfPlayers[selected].Lx = ListOfPlayers[selected].Lx + SpotsToMove
                    print("22")
                    ready = ListOfPlayers[selected].Lx
                    for j in range(len(ListOfPlayers)):
                        if ListOfPlayers[selected].Lx == ListOfPlayers[j].Lx and ListOfPlayers[selected].color != ListOfPlayers[j].color:
                            ListOfPlayers[j].Lx = -1
                            ListOfPlayers[selected].Lx = ready
                    teamTurn = 1
            
    ignorer = 0


    for i in range(len(ListOfPlayers)):
        for j in range(len(ListOfPlayers)):
            if ListOfPlayers[i].Lx == ListOfPlayers[j].Lx and ListOfPlayers[i].color != ListOfPlayers[j].color and teamTurn == 1:
                ListOfPlayers[j].Lx = -1
                print("Terminated " + j)

            if ListOfPlayers[i].Lx == ListOfPlayers[j].Lx and ListOfPlayers[i].color != ListOfPlayers[j].color and teamTurn == 2:
                ListOfPlayers[i].Lx = -1
                print("Terminated" + i)


        
    print('')
    
    print('')
    print('')
    print('')
                

gameInit()

while True == True:
    drawBoard()
    GameUpdate()
    print(ListOfPlayers[5].looped)
