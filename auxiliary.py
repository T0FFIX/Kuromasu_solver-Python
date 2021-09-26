def extractMap(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temporary 1d array

    height = int(temp[0])  # height of the map
    width = int(temp[1])  # width of the map
    arr = []
    temp = temp[2:]  # rid off unnecessary width and height
    for i in range(0, width * height):
        arr.append(int(temp[i]))  # place it into a new array

    return arr


def getMapSizes(mapName):
    file = open(mapName, "r")
    data = file.read()  # read whole file to string
    file.close()
    temp = data.split(',')  # split data to temporary 1d array

    height = int(temp[0])  # pass the height of the map
    width = int(temp[1])  # pass the width of the map

    sizes = [height, width]
    return sizes


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