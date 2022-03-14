import subprocess as sp
from sys import exit
from time import sleep

from pvp import countdown

charList = [
    ("1", "Mario"),
    ("2", "Luigi"),
    ("3", "Bowser"),
    ("4", "Peach"),
]

def init():
    global p1Char, p2Char, p1HP, p2HP, p1MP, p2MP, p1Potions, p2Potions, p1Red, p2Red, p1Blue, p2Blue, p1Green, p2Green, p1Attack, p2Attack, p1Defense, p2Defense, playerTurn
    p1Char = ""
    p2Char = ""
    p1HP = 60
    p2HP = 60
    p1MP = 0
    p2MP = 0
    p1Potions = 1
    p2Potions = 1
    p1Red = 1
    p2Red = 1
    p1Blue = 1
    p2Blue = 1
    p1Green = 1
    p2Green = 1
    p1Attack = 1
    p2Attack = 1
    p1Defense = 0
    p2Defense = 0
    playerTurn = ""
def clear():
    sp.call('cls', shell=True)
    
def mainScreen():
    clear()
    print("Python PVP v1.1")

def mainMenu():
    print("1 - Play Game")
    print("2 - Exit")
    print("")
    ans = int(input("Enter the number for desired action: "))
    if ans == 1:
        startGame()
    elif ans == 2:
        exit()
    else:
        print("Please enter 1 or 2")
        mainMenu()
        
def chooseChar(charList):
    global p1Char
    global p2Char
    clear()
    
    print("These are your fighters, choose wisely!")
    #print all fighters that can be chosen
    for i in charList:
        (num, char) = i
        print(num, " - ", char)
    #prompt P1 to choose fighter
    print("Player 1, choose your fighter!")
    n = int(input("Enter the number that matches your fighter: "))
    p1Char = charList[n-1][1]
    print("Player 1 chose ", p1Char)
    
    #prompt P2 to choose fighter
    print("Player 2, choose your fighter!")
    n = int(input("Enter the number that matches your fighter: "))
    p2Char = charList[n-1][1]
    print("Player 2 chose ", p2Char)
    
    continueGame()

def continueGame():
    inp = input("Shall we continue? (y/n): ")
    if inp.lower() == "y":
        clear()
    elif inp.lower() == "n":
        chooseChar()
    else: 
        print("Please enter 'y' or 'n'")
        continueGame()
        
def p1Turn():
    clear()
    if((p1HP > 0) and (p2HP > 0)):
        print("")
        print("Fighter Stats:")
        print("----------------")
        print(p1Char + "'s HP is " + str(p1HP))
        print(p1Char + "'s MP is " + str(p1MP))
        print(p2Char + "'s HP is " + str(p2HP))
        print(p2Char + "'s MP is " + str(p2MP))
        print("----------------\n")
        print("Player 1's turn: ")
        
        p1Action()
        sleep(3)
        p2Turn()
        
    elif p1HP <= 0:
        print("Player 2 wins!")
        gameOver()
    elif p2HP <= 0:
        print("Player 1 wins!")
        gameOver()
        
def p2Turn():
    clear()
    if((p1HP > 0) and (p2HP > 0)):
        print("")
        print("Fighter Stats:")
        print("----------------")
        print(p1Char + "'s HP is " + str(p1HP))
        print(p1Char + "'s MP is " + str(p1MP))
        print(p2Char + "'s HP is " + str(p2HP))
        print(p2Char + "'s MP is " + str(p2MP))
        print("----------------\n")
        print("Player 2's turn: ")
        
        p2Action()
        sleep(3)
        p1Turn()
        
    elif p1HP <= 0:
        print("Player 2 wins!")
        gameOver()
    elif p2HP <= 0:
        print("Player 1 wins!")
        gameOver()
        
def p1Action():
    print("What do you want to do?\n")
    print("1 - Basic Attack")
    print("2 - Special Attack")
    print("3 - Use Item")
    print("4 - Surrender")
    
    n = input()
    if n == 1:
        p1Basic()
    elif n == 2:
        p1Special()
    elif n == 3:
        p1Item()
    elif n == 4:
        p1Surrender()
    else: 
        print("Please enter the number corresponding with your action.")
        p1Action()
        
def p2Action():
    print("What do you want to do?\n")
    print("1 - Basic Attack")
    print("2 - Special Attack")
    print("3 - Use Item")
    print("4 - Surrender")
    
    n = input()
    if n == 1:
        p2Basic()
    elif n == 2:
        p2Special()
    elif n == 3:
        p2Item()
    elif n == 4:
        p2Surrender()
    else: 
        print("Please enter the number corresponding with your action.")
        p2Action()
        
def startGame():
    init()
    chooseChar()
    print("Player 1 - " + p1Char)
    print("Player 2 - " + p2Char)
    countdown(3)
    clear()
    p1Turn()
    
def p1Basic():
    global p1HP
    print("")
    print(p1Char + " attacks!")
    print(p2Char + " loses " + str(p1Attack*10 - p2Defense*5) + " HP!")
    