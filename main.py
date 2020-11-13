import random
import time
import sys

mapsFolder = "maps/"  # folder with maps to read from


def checkQuality(board, width, height):
    error = 0
    for i in range(0, len(board)):
        # Rule 1: Each number on the board represents the number of white cells that can be seen from that cell,
        # including itself. A cell can be seen from another cell if they are in the same row or column, and there
        # are no black cells between them in that row or column.
        if board[i] != 1 and board[i] != 0:
            count = 0  # it automaticaly countes itself
            iterator = 0
            # i = 0
            #0,0,0,0,3,0,2,0,0,3,0,4,0,0,0,0 ///4

            # check right
            while True:
                if i % width + iterator < width and board[i + iterator] != 1:
                    count += 1
                    iterator += 1
                else:
                    break
            iterator = 0
            # check down
            while True:
                if i + width*iterator < width * height and board[i + width*iterator] != 1:
                    count += 1
                    iterator += 1
                else:
                    break
            iterator = 0
            # check left
            while True:
                # if i-iterator >= 0:  # todo TO ZMIENIONE INNE OD RESZTY
                if i % width - iterator < width and i - iterator >= 0 and board[i - iterator] != 1:
                    count += 1
                    iterator += 1
                else:
                    break
            iterator = 0
            # check up
            while True:
                if i - width*iterator < width * height and i - width*iterator >= 0 and board[i - width*iterator] != 1:
                    count += 1
                    iterator += 1
                else:
                    break
            count = count - 3
            if board[i] != count:
                error += 1
                break

        # Rule 2: No two black cells may be horizontally or vertically adjacent.
        elif board[i] == 1:  # check self if on black cell
            if board[i+1] is not None and board[i+1] == 1:  # check right
                error += 1
                break
            elif board[i+1] is not None and board[i+width] == 1:  # check down
                error += 1
                break
            elif board[i+1] is not None and board[i-1] == 1:  # check left
                error += 1
                break
            elif board[i+1] is not None and board[i-width] == 1:  # check up
                error += 1
                break

        # Rule 3: All the white cells must be connected horizontally or vertically.
        elif board[i] == 0:
            counter = 0

            # check right
            if board[i + 1] is None:
                counter += 1
            elif board[i + 1] == 1:
                counter += 1

            # check down
            if board[i + width] is None:
                counter += 1
            elif board[i + width] == 1:
                counter += 1

            # check left
            if board[i - 1] is None:
                counter += 1
            elif board[i - 1] == 1:
                counter += 1

            # check up
            if board[i - width] is None:
                counter += 1
            elif board[i - width] == 1:
                counter += 1

            if counter == 4:
                error += 1

    # Return number of errors
    return error


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


def generateRandomSolution(board, width, height):  # playerBoard => cleanBoard
    errors = checkQuality(board, width, height)
    while errors != 0:
        for i in range(0, len(board)):
            if board[i] == str(0):  # TODO przekonwertowac wszystkie stringi do numerow w projekcie
                board[i] = str(random.randint(0, 1))
        print(errors)  # TODO debug

    return board


def printSolution(cleanBoard, actualBoard, height, width):  # todo fancy feature, poprawic na 2d
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


def insertNumbers(board, cleanBoard):
    for i in range(len(cleanBoard)):
        if int(cleanBoard[i]) >= 2:
            board[i] = cleanBoard[i]
    return board


def bruteForce(cleanBoard, width, height):
    for i in range(0, 2 ** len(cleanBoard)):
        board = []
        generated = str(bin(i))
        generated = appendWithZeros(generated[2:], len(cleanBoard))

        for letter in generated:
            board.append(int(letter))  # todo jak nie zadziala daj extend zamiast append
        board = insertNumbers(board, cleanBoard)

        if checkQuality(board, width, height) == 0:
            return board


def main():
    filename = "1.txt"
    mapOutput = "output.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        mapOutput = sys.argv[2]

    mapName = mapsFolder + filename
    cleanBoard = extractMap(mapName)  # empty map
    width = getMapSizes(mapName)[0]
    height = getMapSizes(mapName)[1]

    start_time = time.time()  # when alghoritm stats working
    # correctBoard = generateRandomSolution(cleanBoard, width, height)
    correctBoard = bruteForce(cleanBoard, width, height)
    work_time = time.time() - start_time

    print("Elapsed alghoritm work time: " + str(work_time))
    printSolution(cleanBoard, correctBoard, width, height)
    saveSolution(correctBoard, mapOutput)


if __name__ == "__main__":
    main()
