import random
import time
import sys

mapsFolder = "maps/"  # folder with maps to read from
mapsAnswersFolder = "maps_answers/"  # folder with answers


# Each number on the board represents the number of white cells that can be seen from that cell, including itself.
# A cell can be seen from another cell if they are in the same row or column,
# and there are no black cells between them in that row or column.
def checkNumberOfWhiteCells(board, width, height):
    error = False
    for i in range(0, len(board)):
        if board[i] != 1 and board[i] != 0:
            count = 1  # it automaticaly countes itself
            iterator = 1
            while i % width + iterator < width and board[i + iterator] != 1:  # check right
                count += 1
                iterator += 1

            while i + width*iterator < width * height and board[i + width*iterator] != 1:  # check down
                count += 1
                iterator += 1

            while i % width - iterator < width and board[i - iterator] != 1:  # check left
                count += 1
                iterator += 1

            while i - width*iterator < width * height and board[i - width*iterator] != 1:  # check up
                count += 1
                iterator += 1

            if board[i] != count:
                error = True
                break
    return error


# No two black cells may be horizontally or vertically adjacent.
def checkAdjustment(board, width):  # two black squares cannot be near themself
    error = False
    for i in range(0, len(board)):
        if board[i] == 1:  # check self if on black cell
            if board[i+1] is not None and board[i+1] == 1:  # check right
                error = True
                break
            elif board[i+1] is not None and board[i+width] == 1:  # check down
                error = True
                break
            elif board[i+1] is not None and board[i-1] == 1:  # check left
                error = True
                break
            elif board[i+1] is not None and board[i-width] == 1:  # check up
                error = True
                break
    return error


# All the white cells must be connected horizontally or vertically.
def checkConectivity(board, width):  # checkes whether all white blocks are connected
    error = False
    for i in range(0, len(board)):
        if board[i] == 0:
            counter = 0

            # check right
            if board[i + 1] is None:
                counter += 1
            else:
                if board[i + 1] == 1:
                    counter += 1

            # check down
            if board[i + width] is None:
                counter += 1
            else:
                if board[i + width] == 1:
                    counter += 1

            # check left
            if board[i - 1] is None:
                counter += 1
            else:
                if board[i - 1] == 1:
                    counter += 1

            # check up
            if board[i - width] is None:
                counter += 1
            else:
                if board[i - width] == 1:
                    counter += 1

            if counter == 4:
                error = True

    return error


def checkRules(board, width, height):  # todo to bedzie w check quality
    if checkAdjustment(board, width) is False or checkConectivity(board, width) is False or \
            checkNumberOfWhiteCells(board, width, height) is False:
        return False


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


def generateRandomSolution(actualBoard, answerBoard):  # playerBoard => cleanBoard
    for i in range(0, len(actualBoard)):
        if actualBoard[i] == str(0):
            actualBoard[i] = str(random.randint(0, 1))

    errors = checkQuality(actualBoard, answerBoard)
    while errors != 0:
        for i in range(0, len(actualBoard)):
            if actualBoard[i] == str(0):
                actualBoard[i] = str(random.randint(0, 1))
        print(errors)

    return actualBoard


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


    for i in range(0, 2 ** size):
        record = str(bin(i))
        record = appendWithZeros(record[2:], size)
        checkRules(record, width, height)
        if checkQuality(record) == 0:
            return record




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

    # generateRandomSolution(cleanBoard, actualAnswerBoard)

    start_time = time.time()  # when alghoritm stats working
    correctBoard = bruteForce(cleanBoard, actualAnswerBoard)
    work_time = time.time() - start_time

    print("Elapsed alghoritm work time: " + str(work_time))
    mapSizes = getMapSizes(mapName)
    printSolution(cleanBoard, correctBoard, mapSizes[0], mapSizes[1])
    saveSolution(correctBoard, mapOutput)


if __name__ == "__main__":
    main()
