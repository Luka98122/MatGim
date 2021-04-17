import random

boardWith = 11
boardHeight = 11
ListOfPlayers = []
a =''
selected = -3
SpotsToMove = -4

teamTurn = 1

class Player:
    def __init__(self, col, num, pos):
        self.color = col
        self.state = 1
        self.safe = 1
        self.number = num
        self.Lx = pos
        self.looped = 0

def gameInit ():
    for i in range(2): #Number of teams
        for j in range(4): #Number of players per team
            if i == 1:
                Color = 0
            else:
                Color = 1
            player = Player(Color, j, -1)
            ListOfPlayers.append(player)
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
    if LxCoords > 39:
        LxCoords = LxCoords - 40
        ListOfPlayers[player].looped = 1
    if LxCoords < 5:
        return(4,10-LxCoords)
    if LxCoords < 9 and LxCoords >= 5:
        return (10-LxCoords-2, 6)
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
                if a[0] == j and a[1] == i and printedPlayer == 0 and ListOfPlayers[y].Lx != -1:
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
    global SpotsToMove
    global selected
    global teamTurn
    cleared = 0

    while True == True:
        try:
            selected = int(input("Confrim moving that pawn, or pick a diffret one. If you see this message a lot you are selecting an invalid pawn."))
            if teamTurn == 1:
                if SpotsToMove == 6 and ListOfPlayers[selected].Lx == -1 and selected < 4:
                    teamTurn = 2
                    ListOfPlayers[selected].Lx = 0
                    return 1

            if teamTurn == 2:
                if SpotsToMove == 6 and ListOfPlayers[selected].Lx == -1 and selected >= 4 and selected < 8:
                    teamTurn = 1
                    ListOfPlayers[selected].Lx = 10
                    return 1

            print(teamTurn)
            for i in range(4):
                 if teamTurn == 1 and selected < 4 and ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[i].Lx:
                    cleared = cleared + 1
            if cleared == 4 and ListOfPlayers[selected].Lx >= 0:
                cleared = 0
                break
            cleared = 0
            for j in range(4,8):
                if teamTurn == 2 and selected >= 4 and selected < 8 and ListOfPlayers[selected].Lx + SpotsToMove != ListOfPlayers[j].Lx:
                    cleared = cleared + 1
            if cleared == 4 and ListOfPlayers[selected].Lx >= 0:
                cleared = 0
                break
            cleared = 0
        except:
                cleared = 0
                print('You entered an invalid input, please try again')

def TeamUpdate():
    global teamTurn
    global selected
    global SpotsToMove
    global a
    SpotsToMove = random.randint(1,6)
    if a == '':
        print("You can move " + str(SpotsToMove) + " spots.")
        print('')
    else:
        while 1 == 1:
            a = input("Bad input. Please try again.")
            if a == '':
                print("You can move " + str(SpotsToMove) + " spots.")
                print('')
                break
    
    print("Team turn is", teamTurn)
    
    z = checkMoves() 
    if z == 0 and teamTurn == 1:
        teamTurn = 2
        return
    if z == 1 and teamTurn == 2:
        teamTurn = 1
        return
    
    l = handleUserInput()
    if l == 1:
        return
    if teamTurn == 1:
        handleUserInput()
        ListOfPlayers[selected].Lx = ListOfPlayers[selected].Lx + SpotsToMove
        for i in range(4, 8):
            if ListOfPlayers[selected].Lx == ListOfPlayers[i].Lx:
                ListOfPlayers[i].Lx == -1
        teamTurn = 2
                
    else:
        if teamTurn == 2:
            handleUserInput()
            ListOfPlayers[selected].Lx = ListOfPlayers[selected].Lx + SpotsToMove
            for i in range(4):
                if ListOfPlayers[selected].Lx == ListOfPlayers[i].Lx:
                    ListOfPlayers[i].Lx = -1
                teamTurn = 1

# Checks if team has possible moves, if the first team doesnt have moves, returns 0, if the second team doesnt have moves returns 1. Otherwise returns 3. 
def checkMoves():
    global teamTurn
    global selected
    global SpotsToMove
    movelessPawns = 0
    for i in range(4):
        if teamTurn == 1 and SpotsToMove != 6 and ListOfPlayers[i].Lx < 0:
            movelessPawns = movelessPawns + 1

    if movelessPawns == 4:
        movelessPawns = 0
        print("Team 1 out of moves")
        return 0
    
    movelessPawns = 0
    for j in range(4,8):
        if teamTurn == 2 and SpotsToMove != 6 and ListOfPlayers[j].Lx < 0:
            movelessPawns = movelessPawns + 1

    if movelessPawns == 4:
        print("Team 2 out of moves")
        movelessPawns = 0
        return 1

    movelessPawns = 0
    return 3

def GameUpdate():
    checkedOff = 0
    global a
    
    for i in range(len(ListOfPlayers)):
        if ListOfPlayers[i].Lx > 39 and ListOfPlayers[i].color == 2:
            ListOfPlayers[i].Lx = ListOfPlayers[i].Lx - 40
            ListOfPlayers[i].looped = 1

        if ListOfPlayers[i].Lx == 39:
            ListOfPlayers[i].looped = 1
                
        if ListOfPlayers[i].Lx >= 39 and ListOfPlayers[i].color == 1:
            ListOfPlayers[i].Lx = -2
            ListOfPlayers[i].looped == 1
        if ListOfPlayers[i].Lx > 9 and ListOfPlayers[i].color == 2 and ListOfPlayers[i].looped == 1:
            ListOfPlayers[i].Lx = -2
        
        if ListOfPlayers[i].looped == 1 and ListOfPlayers[i].color == 1:
            checkedOff = checkedOff + 1
            if checkedOff == 4:
                print("PRVI TEAM je pobedio")
                exit()
            
        if ListOfPlayers[4].Lx == -2 and ListOfPlayers[5].Lx == -2 and ListOfPlayers[6].Lx == -2 and ListOfPlayers[7].Lx == -2:
            print("DRUGI Team je pobedio")
            exit()
    checkedOff = 0
    a = input("Hit enter to throw the dice")        
    TeamUpdate()

    print('')
    print('')
    print('')
    print('')
                
gameInit()

while True == True:
    drawBoard()
    GameUpdate()
