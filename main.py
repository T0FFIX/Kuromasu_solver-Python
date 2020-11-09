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

    width = int(temp[0])
    height = int(temp[1])

    arr = []
    temp = temp[2:]  # rid off unnessesary width and height
    for i in range(0, width * height - 2):
        arr.append(str(temp[i]))

    return arr


def checkQuality(actualBoard, answerBoard):
    qualityScore = 0
    for i in range(0, len(actualBoard)):
        if actualBoard[i] != answerBoard[i]:
            qualityScore += 1

    return qualityScore


def generateRandomSolution(playerBoard): #playerBoard => cleanBoard
    for i in range(0, len(playerBoard)):
        if playerBoard[i] == str(0):
            playerBoard[i] = str(random.randint(0, 1))

    return playerBoard


def printSolution(cleanBoard, actualBoard, height, width):
    print("Input: ")
    for el in cleanBoard:
        print(el + " ", end="")

    print("\n" + "Output: ")
    for el in actualBoard:
        print(el + " ", end="")


def getMapSizes(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temoporary 1d array

    width = int(temp[0])
    height = int(temp[1])

    arr = [width, height]
    return arr


def saveSolution(solution, filename):
    file = open(filename, "w")
    for i in range(0, len(solution)):
        file.write(solution[i])
    file.close()


def appendWithZeros(element, size):
    new = ""
    for i in range(0, size - len(element)):
        new += str(0)

    new += element
    return list(new)


# size is number of white squares on map
def getBinaryPermutations(size):
    collection = []
    for i in range(0, 2 ** size):
        record = str(bin(i))
        collection.append(appendWithZeros(record[2:], size))

    return collection


def insertNumbers(cleanBoard, answerBoard):
    for i in range(len(cleanBoard)):
        if int(cleanBoard[i]) >= 2:
            answerBoard[i] = cleanBoard[i]


def bruteForce(cleanBoard, actualAnswerBoard):
    size = len(cleanBoard)
    answerBoard = getBinaryPermutations(size)

    for actualBoard in answerBoard:
        insertNumbers(cleanBoard, actualBoard)
        if checkQuality(actualBoard, actualAnswerBoard) == 0:
            return actualBoard


def main():
    filename = "1.txt"
    mapOutput = "output.txt"
    mapAnswersName = mapsAnswersFolder + filename

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        mapOutput = sys.argv[2]

    mapName = mapsFolder + filename

    cleanBoard = extractMap(mapName)  # empty map
    actualAnswerBoard = extractMap(mapAnswersName)

    start_time = time.time()  # when alghoritm stats working
    correctBoard = bruteForce(cleanBoard, actualAnswerBoard)
    work_time = time.time() - start_time

    print("Elapsed alghoritm work time: " + str(work_time))
    mapSizes = getMapSizes(mapName)
    printSolution(cleanBoard, correctBoard, mapSizes[0], mapSizes[1])
    saveSolution(correctBoard, mapOutput)


if __name__ == "__main__":
    main()
