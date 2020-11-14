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
            # check right
            # WORKING
            while True:
                try:
                    iterator += 1
                    if i % width + iterator < width and board[i + iterator] != 1:
                        count += 1
                    elif i % width + iterator >= width or board[i + iterator] == 1:
                        break
                except IndexError:
                    break
            iterator = 0

            # check down
            #WORKING
            while True:
                try:
                    iterator += 1
                    if i + width * iterator <= width*height and board[i + width * iterator] != 1:
                        count += 1
                    elif i + width * iterator > width*height or board[i + width * iterator] == 1:
                        break
                except IndexError:
                    break
            iterator = 0

            # check left
            # WORKING
            while True:
                try:
                    iterator += 1
                    if i % width - iterator >= 0 and board[i - iterator] != 1:
                        count += 1
                    elif i % width - iterator < 0 or board[i - iterator] == 1:
                        break
                except IndexError:
                    break
            iterator = 0

            # check up
            #WORKING
            while True:
                try:
                    iterator += 1
                    if i - width * iterator >= 0 and board[i - width * iterator] != 1:
                        count += 1
                    elif i - width * iterator < 0 or board[i - width * iterator] == 1:
                        break
                except IndexError:
                    break

            count = count + 1
            if board[i] != count:
                error += 1
                # break

        # Rule 2: No two black cells may be horizontally or vertically adjacent.
        elif board[i] == 1:  # check self if on black cell
            try:
                if (i % width) + 1 < width and board[i + 1] == 1:  # check right
                    error += 1

                elif i + width < width * height and board[i + width] == 1:  # check down
                    error += 1

                elif (i % width) - 1 > 0 and board[i - 1] == 1: # check left
                    error += 1

                elif i - width > 0 and board[i - width] == 1:  # check up
                    error += 1

            except IndexError:
                print("", end="")

        # Rule 3: All the white cells must be connected horizontally or vertically.
        elif board[i] == 0:
            counter = 0

            try:
                if board[i + 1] == 1:  # check right
                    counter += 1
                elif (i % width) + 1 > width:
                    counter += 1
            except IndexError:
                counter += 1

            try:
                if board[i + width] == 1:  # check down
                    counter += 1
                elif i + width > width * height:
                    counter += 1
            except IndexError:
                counter += 1

            try:
                if board[i - 1] == 1: # check left
                    counter += 1
                elif (i % width) - 1 < 0:
                    counter += 1
            except IndexError:
                counter += 1

            try:
                if board[i - width] == 1:  # check up
                    counter += 1
                elif i - width < 0:
                    counter += 1
            except IndexError:
                counter += 1

            if counter == 4:
                error += 1
    # Return number of errors
    # print(error)
    return error


def extractMap(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temoporary 1d array

    height = int(temp[1])
    width = int(temp[0])

    arr = []
    temp = temp[2:]  # rid off unnessesary width and height
    for i in range(0, width * height):
        arr.append(int(temp[i]))

    return arr


def getMapSizes(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temoporary 1d array

    width = int(temp[1])
    height = int(temp[0])

    arr = [width, height]
    return arr


def generateRandomSolution(board, width, height):  # playerBoard => cleanBoard
    usedBoard = board.copy()
    errors = checkQuality(usedBoard, width, height)
    while errors != 0:
        for i in range(0, len(usedBoard)):
            if usedBoard[i] == 0 or usedBoard[i] == 1:
                usedBoard[i] = random.randint(0, 1)
        errors = checkQuality(usedBoard, width, height)
    return usedBoard


def printSolution(cleanBoard, correctBoard, width, height):
    print("Input: ")
    for k in range(0, height):
        for i in range(0, width):
            print(str(cleanBoard[k * width + i]) + " ", end="")
        print("")

    print("\n" + "Output: ")
    for k in range(0, height):
        for i in range(0, width):
            print(str(correctBoard[k * width + i]) + " ", end="")
        print("")

def saveSolution(cleanBoard, correctBoard, width, height, work_time, mapOutput):
    file = open(mapOutput, "w")

    file.write("Input:" + "\n")
    for k in range(0, height):
        for i in range(0, width):
            file.write(str(cleanBoard[k * width + i]) + " ")
        file.write("\n")

    file.write("\n" +"Solution:" + "\n")
    for k in range(0, height):
        for i in range(0, width):
            file.write(str(correctBoard[k * width + i]) + " ")
        file.write("\n")

    file.write("\n" + "Time:" + "\n")
    file.write(str(work_time))
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


def bruteForce(cleanBoard, width, height):  # TODO zepsute, naprawic
    for i in range(0, 2 ** len(cleanBoard)):
        board = []
        generated = str(bin(i))
        generated = appendWithZeros(generated[2:], len(cleanBoard))

        for letter in generated:
            board.append(int(letter))
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
    correctBoard = generateRandomSolution(cleanBoard, width, height)
    # correctBoard = bruteForce(cleanBoard, width, height)

    work_time = time.time() - start_time

    printSolution(cleanBoard, correctBoard, width, height)
    print()
    print("Elapsed alghoritm work time: " + str(work_time))

    saveSolution(cleanBoard, correctBoard, width, height, work_time, mapOutput)


if __name__ == "__main__":
    main()
