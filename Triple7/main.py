import random

def cherryWinnings(num):
    cherryCost = 1
    totalWin = cherryCost * num
    return totalWin

def lineWinnings(symbol, symbolCost):
    for i in range(len(symbolCost)):
        if symbol == symbolCost[i][0]:
            return symbolCost[i][1]
    
def checkWin(rowWin, symbolCost):
    cherryCount = 0

    # check for cherries
    for i in range(len(rowWin)):
        textCheck = rowWin[i]
        if textCheck == "cherry":
            cherryCount += 1

    if cherryCount > 0:
        return cherryWinnings(cherryCount)
    
    # check for a match three
    if rowWin[0] == rowWin[1]:
        if rowWin[1] == rowWin[2]:
            return lineWinnings(rowWin[0], symbolCost)
        else:
            return 0
    else:
        return 0

def randomize(symbolList):
    someNum = random.randint(0, len(symbolList) - 1)  
    return symbolList[someNum]

def gameLoop(credits, symbolList, symbolCost):
    userCredits = credits - 1

    while True:

        firstCol = randomize(symbolList)
        secondCol = randomize(symbolList)
        thirdCol = randomize(symbolList)

        print("\n")
        print(firstCol, secondCol, thirdCol, sep="   |   ")

        mainLine = [firstCol, secondCol, thirdCol]

        textWin = checkWin(mainLine, symbolCost)

        if textWin == 1:
            print("\nYou won: ", textWin, " credit")
        else:
            print("\nYou won: ", textWin, " credits")

        userCredits += textWin
        print("\n Current Credits: ", userCredits, "\n")

        if userCredits <= 0:
            print("No more credits!")
            return 0

        playAgain = input("input 'q' to quit: ")
        if playAgain == "q":
            return userCredits
        else:
            userCredits -= 1


def main():

    symbolList = ["cherry", "  7s  ", " bell ", " tree ", "  __  "]
    symbolCost = [("  7s  ", 777), (" bell ", 100), (" tree ", 50), ("  __  ", 0)]
    credits = int(input("How much to insert? "))
    endCredits = gameLoop(credits, symbolList, symbolCost)

    if endCredits > 0:
        print("Game over! Ending credits: ", endCredits)
    else:
        print("Game over! You went broke!")
    


if __name__ == "__main__":
    main()