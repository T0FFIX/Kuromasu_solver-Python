import random
import time
import sys

mapsFolder = "maps/"  # folder with maps to read from
mapsAnswersFolder = "maps_answers/"  # folder with answers

def extractMap(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temoporary 1d array

    arr = []
    counter = 2  # actual position in splitted array, width and height is not counted
    width = int(temp[0])
    height = int(temp[1])
    for i in range(height):
        col = []
        for j in range(width):
            col.append(arr[counter])
            counter += 1
        arr.append(col)

    return arr

def checkScore(playerBoard, correctMap):
    qualityScore = 0
    for col in range(0, len(correctMap)):
        for row in range(0, len(correctMap[col])):
            if playerBoard[col][row] != correctMap[col][row]:
                qualityScore += 1

    return qualityScore  # returns number of mistakes, 0 is ideal solution

def randomGeneretedSolution(playerBoard):
    for col in range(0, len(playerBoard)):
        for row in range(0, len(playerBoard[col])):
            if playerBoard[col][row] == 0:
                playerBoard[col][row] = random.randint(0, 1)

    return playerBoard

def forcedSolution(solution):
    return 0

def printSolution(cleanBoard, actualBoard, mistakesNumber):
    for col in range(0, len(cleanBoard)):
        for row in range(0, len(cleanBoard[col])):
            print(cleanBoard[col][row])

    for col in range(0, len(actualBoard)):
        for row in range(0, len(actualBoard[col])):
            print(actualBoard[col][row])

    print(mistakesNumber)

def saveSolution(solution, filename):
    file = open(filename, "w")
    for col in range(0, len(solution)):
        for row in range(0, len(solution[col])):
            file.write(solution[col][row])
    file.close()

def main():
    mapName = "/maps/1.txt"
    mapOutput = "output.txt"
    if len(sys.argv) >= 2:
        mapName = sys.argv[1]
        mapOutput = sys.argv[2]

    cleanBoard = extractMap(mapName)  # empty map
    correctBoard = extractMap(mapName)  # fully correct map

    start_time = time.time()  # when alghoritm stats working
    actualBoard = randomGeneretedSolution(cleanBoard)
    mistakesNumber = checkScore(actualBoard, correctBoard)
    while mistakesNumber != 0:
        actualBoard = randomGeneretedSolution(cleanBoard)
        printSolution(cleanBoard, actualBoard, mistakesNumber)
        mistakesNumber = checkScore(actualBoard, correctBoard)

    work_time = time.time() - start_time
    print("Elapsed alghoritm work time: " + str(work_time))
    saveSolution(actualBoard, mapOutput)

if __name__ == "__main__":
    main()