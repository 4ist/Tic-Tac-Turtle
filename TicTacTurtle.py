
from turtle import *
import time
import math


mode("logo")
speed(0)
width(3)

ht()
size = 300
pos = int(size/2) # half of the border height
oThird = int(size/6)    # half of a single square's height
sqrLst = []



stateLst = []
for i in range(3):
    tmplst = []
    for i in range(3):
        tmplst.append(-99)
    stateLst.append(tmplst)

gameOver = False

movecount = 0
winner = ""



def drawSqr(sqrSize):
    pu()
    goto(pos,pos)
    pd()
    setheading(180)
    
    for i in range(4):
        fd(sqrSize)
        rt(90)
    

def drawGrid(sqrsize):
    global pos
    
    global oThird
    
    for i in (-1,1):
        pu()
        goto(pos,i*oThird)
        pd()
        goto(-pos,i*oThird)
        
    for i in (-1,1):
        pu()
        goto(i*oThird,pos)
        pd()
        goto(i*oThird,-pos)
        
def getSqrCoords():
    global oThird
    global sqrLst
    for x in (-2*oThird, 0, 2*oThird):
        column = []
        for y in (-2*oThird, 0, 2*oThird):
            column.append((x,y))
        sqrLst.append(column)
        
def drawX(sqrX,sqrY):
    global oThird    
    global sqrLst
    global stateLst
    
    print("drawX",sqrX,sqrY)
    stateLst[sqrX][sqrY] = 1
    pencolor("blue")
    

    (x,y) = sqrLst[sqrX][sqrY]
    
    pu()
    goto((x-oThird)+5,(y-oThird)+5)
    pd()
    goto((x+oThird)-5,(y+oThird)-5)
    
    pu()
    goto((x+oThird)-5,(y-oThird)+5)
    pd()
    goto((x-oThird)+5,(y+oThird)-5)
    
def drawO(sqrX,sqrY):
    global oThird    
    global sqrLst
    global stateLst
    
    stateLst[sqrX][sqrY] = 0
    pencolor("red")
    
    (x,y) = sqrLst[sqrX][sqrY]
    pu()
    goto(x,y-.9*oThird)
    setheading(90)
    pd()
    circle(.9*oThird)
    

    
def checkState():
    global stateLst
    global gameOver
    global pos
    global oThird
    global winner
    
    for i in range(len(stateLst)):
        latCheck = sum(stateLst[i])
        if latCheck in [0, 3]:
            drawPerpVictory("u", i)
            #print(stateLst)
            if latCheck == 3:
                winner = "X"
                gameOver = True
            if latCheck == 0:
                winner = "O"
                gameOver = True
            
        vertCheck = stateLst[0][i] + stateLst[1][i] + stateLst[2][i]
        if vertCheck in [0, 3]:
            drawPerpVictory("r", i)
            #print(stateLst)
            if vertCheck == 3:
                winner = "X"
                gameOver = True
            if vertCheck == 0:
                winner = "O"
                gameOver = True
            
        
            
    sumUp = stateLst[0][0] + stateLst[1][1] + stateLst[2][2]     
    sumDown = stateLst[2][0] + stateLst[1][1] + stateLst[0][2]
    
    if 3 in (sumUp,sumDown):
        print("X wins")
        winner = "X"
        gameOver = True
        
    if 0 in (sumUp,sumDown):
        print("O wins")
        winner = "O"
        gameOver = True
        
    if sumUp in (0,3):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        drawDiagVictory("up")
    if sumDown in (0,3):
        drawDiagVictory("down")
        
def drawDiagVictory(direction):
    pencolor("orange")
    
    pu()
    if direction == "up":
        print("UPPPPP")
        goto(int(-2*oThird), -pos-10)
        setheading(90)
    if direction == "down":
        goto(-pos-10, int(2*oThird))
        setheading(180)
    pd()
    
    diagDist = math.sqrt(2*(4*oThird)**2)
    circle(oThird+10, 45)
    fd(diagDist)
    circle(oThird+10, 180)
    fd(diagDist)
    circle(oThird+10, 135)    
        
def drawPerpVictory(direction,column):
    
    pencolor("orange")
    
    pu()
    if direction == "u":
        goto(int((column-1)*2*oThird), -pos-10)
        setheading(90)
    if direction == "r":
        goto(-pos-10, int((column-1)*2*oThird))
        setheading(180)
    pd()
    
    circle(oThird+10, 90)
    fd(4*oThird)
    circle(oThird+10, 180)
    fd(4*oThird)
    circle(oThird+10, 90)        
 
def popTo(x,y):
    tempx = -99
    tempy = -99
    
    if gameOver:
        return displayWinner()
    if x not in range(-pos,pos):
        print("Out of range; make a valid move")
        return 1
    if y not in range(-pos,pos):
        print("Out of range; make a valid move")
        return 1
        
    for i in (x, y):
        if -pos <= i and i <= -oThird:
            tempy = 0
        elif -oThird <=i and i <= oThird:
            tempy = 1
        elif oThird <= i and i <= pos:
            tempy = 2
        if tempy != -99 and tempx == -99:
            tempx = tempy
        
    print(tempx,tempy)
    if tempx != -99 and tempy != -99:
        rulescheck(tempx,tempy)
    
def rulescheck(x,y):        
    global movecount
    global stateLst
    
    if movecount % 2 == 1:
        currentPlayer = "X" 
    else:
        currentPlayer = "O"
    print(f"Choose a square for {currentPlayer}")
   
    if stateLst[x][y] != -99:
        print("That square has already been chosen")
    else:
        movecount +=1
        
        if movecount % 2 == 0:
            drawX(x,y)
        else:
            drawO(x,y)
        checkState()
        if movecount >= 9 and not gameOver:
            print("The game is a draw")
            displayWinner()
    if gameOver:
        displayWinner()
        print(f"~~~~Player {winner} has won on turn {movecount}~~~~")
    
def displayWinner():
    global winner
    texter = Turtle()
    texter.ht()
    texter.pu()
    texter.speed(0)
    texter.goto(0,4*oThird)
    texter.pencolor("black")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~WINNER", winner)
    if winner == "X":
        texter.pencolor("blue")
    if winner == "O":
        texter.pencolor("red")
    if winner == "":
        texter.write("The game is a draw", False, "center", ("Arial", 24, "normal"))
    else:
        texter.write(f"The Winner is {winner}", False, "center", ("Arial", 24, "normal"))
    
 # TODO
 # Enable socket communication (ezpz)
 # allow the games to talk to eachother
    
drawSqr(size)
drawGrid(size)
getSqrCoords()


onscreenclick(popTo)

done()

