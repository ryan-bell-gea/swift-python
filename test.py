charList = [
    ("1", "Mario"),
    ("2", "Luigi"),
    ("3", "Bowser"),
    ("4", "Peach"),
]
global p1Char, p2Char, p1HP, p2HP, p1MP, p2MP
p1Char = ""
p2Char = ""
p1HP = 60
p2HP = 60
p1MP = 0
p2MP = 0

def chooseChar(charList):
    global p1Char
    global p2Char
    
    
    print("These are your fighters, choose wisely!")
    #print all fighters that can be chosen
    for i in charList:
        (num, char) = i
        print(num, " - ", char)
    #prompt P1 to choose fighter
    print("Player 1, choose your fighter!")
    n = int(input("Enter the number that matches your fighter: "))
    p1Char = charList[n-1][1]
    print("Player 1 chose", p1Char)
    
    #prompt P2 to choose fighter
    print("Player 2, choose your fighter!")
    n = int(input("Enter the number that matches your fighter: "))
    p2Char = charList[n-1][1]
    print("Player 2 chose", p2Char)

def p1Turn():
    
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

chooseChar(charList)
p1Turn()
