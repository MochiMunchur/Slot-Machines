import random

def lineWinnings(symbol, symbolCost):
    for i in range(len(symbolCost)):
        if symbol == symbolCost[i][0]:
            return symbolCost[i][1]
    
def checkWin(rowWin, symbolCost):
    
    # check for a match three
    if rowWin[0] == rowWin[1]:
        if rowWin[1] == rowWin[2]:
            return lineWinnings(rowWin[0], symbolCost) 


    if rowWin[0] != "  __  ":
        if rowWin[1] != "  __  ":
            if rowWin[2] != "  __  ":
                return 5
            else:
                return 0
        else:
            return 0
    else:
        return 0


def randomize(symbolList):
    someNum = random.randint(0, len(symbolList) - 1)  
    return symbolList[someNum]

def gameLoop(credits, symbolList, symbolCost):
    userCredits = credits - 5

    while True:

        nineSlot = [None] * 9
        for i in range(len(nineSlot)):
            nineSlot[i] = randomize(symbolList)

        print("\n")
        firstRow = nineSlot[:3]
        secondRow = nineSlot[3:6]
        thirdRow = nineSlot[6:]
        topLeft = [firstRow[0], secondRow[1], thirdRow[2]]
        botLeft = [thirdRow[0], secondRow[1], firstRow[2]]

        #print(nineSlot)
        print(firstRow)
        print(secondRow)
        print(thirdRow)
        print("\n")

        totalWin = 0
        totalWin += checkWin(firstRow, symbolCost)
        totalWin += checkWin(secondRow, symbolCost)
        totalWin += checkWin(thirdRow, symbolCost)
        totalWin += checkWin(topLeft, symbolCost)
        totalWin += checkWin(botLeft, symbolCost)

        if totalWin == 1:
            print("\nYou won: ", totalWin, " credit")
        else:
            print("\nYou won: ", totalWin, " credits")

        userCredits += totalWin
        print("\n Current Credits: ", userCredits, "\n")

        if userCredits <= 0:
            print("No more credits!")
            return 0

        playAgain = input("input 'q' to quit: ")
        if playAgain == "q":
            return userCredits
        else:
            userCredits -= 5


def main():

    barList = [" bar  "] * 3
    doubleBarList = ["barbar"] * 2
    tripleBarList = ["tribar"] * 1
    emptySlotList = ["  __  "] * 10

    symbolList = barList + doubleBarList + tripleBarList + emptySlotList

    #symbolList = [" bar  ", " bar  ", " bar  ", "barbar", "barbar", "tribar","  __  ", "  __  ", "  __  ", "  __  "]
    symbolCost = [(" bar  ", 50), ("barbar", 100), ("tribar", 250), ("  __  ", 0)]
    credits = int(input("How much to insert? "))
    endCredits = gameLoop(credits, symbolList, symbolCost)

    if endCredits > 0:
        print("Game over! Ending credits: ", endCredits)
    else:
        print("Game over! You went broke!")
    


if __name__ == "__main__":
    main()