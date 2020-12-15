import visuals
import random
import time
import sys
import math

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


def bruteForce(cleanBoard, width, height):
    for i in range(0, 2 ** len(cleanBoard)):
        board = []
        generated = str(bin(i))
        generated = appendWithZeros(generated[2:], len(cleanBoard))

        for letter in generated:
            board.append(int(letter))
        board = insertNumbers(board, cleanBoard)

        if checkQuality(board, width, height) == 0:
            return board


def generateRandomSolution(board, width, height):
    errors = checkQuality(board, width, height)
    while errors != 0:
        for i in range(0, len(board)):
            if board[i] == 0 or board[i] == 1:
                board[i] = random.randint(0, 1)
        errors = checkQuality(board, width, height)
    return board


def randomiseMap(board, width, height):
    for i in range(0, len(board)):
        if board[i] == 0 or board[i] == 1:
            board[i] = random.randint(0, 1)
    return board


def generateClimbingSolution(board, width, height):
    errors = checkQuality(board, width, height)
    while errors != 0:
        cleanBoard = board.copy()
        best_neighbour = []
        quality = 99  # error indicator
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = 1
                if quality > checkQuality(board, width, height):
                    best_neighbour = board.copy()
            elif board[i] == 1:
                board[i] = 0
                if quality > checkQuality(board, width, height):
                    best_neighbour = board.copy()
            board = cleanBoard.copy()
        neighbour_quality = checkQuality(best_neighbour, width, height)
        if neighbour_quality < errors:
            errors = neighbour_quality
            board = best_neighbour.copy()
        elif neighbour_quality >= errors:
            board = best_neighbour.copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
    return board


def generateTabuSolution(board, width, height):
    tabu_list = [board]
    errors = checkQuality(board, width, height)
    while errors != 0:
        cleanBoard = board.copy()
        best_neighbour = []
        quality = 99  # error indicator
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = 1
                if quality > checkQuality(board, width, height) and not tabu_list.__contains__(board):
                    best_neighbour = board.copy()
            elif board[i] == 1:
                board[i] = 0
                if quality > checkQuality(board, width, height) and not tabu_list.__contains__(board):
                    best_neighbour = board.copy()
            board = cleanBoard.copy()

        if not best_neighbour:  # if best_neighbour is empty -> all neighbours are tabu
            return board
        tabu_list.append(best_neighbour)
        board = best_neighbour.copy()
        errors = checkQuality(board, width, height)

    return board


def generateSimmannealingSolution(board, width, height):
    temperature_formula = lambda temp: 1 / iterations
    iterations = 10000
    temperature = 120

    board = board.copy()
    all_neighbors = []

    for k in range(0, iterations):
        for i in range(0, len(board)):
            local_board = board.copy()
            if local_board[i] == 0:
                local_board[i] = 1
            elif local_board[i] == 1:
                local_board[i] = 0
            else:
                continue
            all_neighbors.append(local_board)

        neighbor = random.choice(all_neighbors)
        cost_diff = checkQuality(board, width, height) - checkQuality(neighbor, width, height)

        if checkQuality(board, width, height) == 0:
            return board

        if cost_diff > 0:
            board = neighbor.copy()
        elif random.uniform(0, 1) < math.exp(cost_diff / temperature):
            board = neighbor.copy()
        temperature = temperature_formula(temperature)

    print("ERROR: The algorithm is stuck and the last solution is: ")
    errors = checkQuality(board, width, height)
    print("Errors number: " + str(errors))
    return board


def generatePopulation(board, population_size):
    #generates a random but unique population of answers
    population = []
    clean_board = board.copy()
    for j in range(0, population_size):
        for i in range(0, len(board)):
            if board[i] == 0 or board[i] == 1:
                board[i] = random.randint(0, 1)
        if not population.__contains__(board):
            population.append(board)
        board = clean_board.copy()

    return population


def sortByQuality(population, width, height):
    #sorts population by how many errors it hase and returns it
    population_qualities = []
    for el in population:
        dict_el = [el, checkQuality(el, width, height)]
        population_qualities.append(dict_el)

    population_qualities = sorted(population_qualities, key=lambda x: x[1], reverse=False)

    population = []
    for el in population_qualities:
        population.append(el[0])
    return population


def generateGeneticSolution(board, width, height, population_size, best_population_percentage, generations_number, mutation_chance):
    population = generatePopulation(board, population_size)     #population of answers for the starting population
    repopulate_number = population_size - round(population_size * best_population_percentage)   #how many answers we need to generate to repopulate
    best_population_number = round(population_size * best_population_percentage)    #how many best answers we want

    # check starting population for an answer
    for el in population:
        if checkQuality(el, width, height) == 0:
            return el

    for k in range(0, generations_number):
        sorted_population = sortByQuality(population, width, height)
        best = sorted_population[0:best_population_number]

        # replace the worst of best population with one of the rest
        worse_element_pass_chance = random.randrange(0, 100)
        if worse_element_pass_chance < 1:
            newOccurrence = random.randrange(best_population_number, len(sorted_population))
            best[len(best)-1] = sorted_population[newOccurrence]

        random_crossing_position = random.randrange(0, len(best)-1)

        dna_first_half = []
        dna_second_half = []
        for el in best:
            dna_first_half.append(el[0:random_crossing_position])
            dna_second_half.append(el[random_crossing_position:])

        new_generation = []
        for i in range(0, repopulate_number):
            random_choice_first_half = random.randrange(0, best_population_number)
            random_choice_second_half = random.randrange(0, best_population_number)

            offspring = dna_first_half[random_choice_first_half].copy()
            offspring.extend(dna_second_half[random_choice_second_half].copy())
            new_generation.append(offspring)

        for i in range(0, round(repopulate_number*mutation_chance)):
            mutated_offspring = random.randrange(0, len(new_generation))
            mutation = new_generation[mutated_offspring]
            mutated_position = random.randrange(0, len(mutation))

            while mutation[mutated_position] > 1:
                mutated_position = random.randrange(0, len(mutation))

            # switches from 0 to 1 and from 1 to 0
            if mutation[mutated_position] == 0:
                mutation[mutated_position] = 1
            else:
                mutation[mutated_position] = 0

        for el in best:
            new_generation.append(el)

        population = new_generation.copy()

        # check last generation for an answer
        for el in population:
            if checkQuality(el, width, height) == 0:
                return el

    # even if we have no answer, return best possible from last generation
    population = sortByQuality(population, width, height)
    print("ERROR: The algorithm is stuck and the last solution from the last generation is: ")
    errors = checkQuality(population[0], width, height)
    print("Errors number: " + str(errors))
    return population[0]


def test_bruteForce(testOutput, board, width, height):
    file = open(testOutput, "w")
    file.close()
    file = open(testOutput, "a")
    file.write("Brute Force Solution Time: " + "\n")
    file.close()
    number = 0
    cleanboard = board.copy()
    whole_time = time.time()  # when alghoritm stats working
    while number < 25:
        single_try = time.time()  # when alghoritm stats working
        correctBoard = bruteForce(board, width, height)
        single_try_time = time.time() - single_try
        number += 1
        board = cleanboard
        file = open(testOutput, "a")
        file.write("Time " + str(number)+ ": " + str(single_try_time)+"\n")
        file.close()

    brute_force_time = time.time() - whole_time
    file = open(testOutput, "a")
    file.write("Brute Force Whole Time: " + str(brute_force_time)+"\n")
    # file.write("Answer: "+str(correctBoard))
    file.write("\n")
    file.close()
    return 0


def test_generateClimbingSolution(testOutput, board, width, height):
    file = open(testOutput, "a")
    file.write("\n")
    file.write("\n")
    file.write("Climbing Solution Time: "+"\n")
    file.close()
    number = 0
    cleanboard = board.copy()
    whole_time = time.time()  # when alghoritm stats working
    while number < 25:
        single_try = time.time()  # when alghoritm stats working
        correctBoard = generateClimbingSolution(board, width, height)
        single_try_time = time.time() - single_try
        number += 1
        board = cleanboard
        file = open(testOutput, "a")
        file.write("Time " + str(number) + ": " + str(single_try_time) + "\n")
        file.close()

    climbing_time = time.time() - whole_time
    file = open(testOutput, "a")
    file.write("Climbing Whole Time: " + str(climbing_time) + "\n")
    # file.write("Answer: " + str(correctBoard))
    file.write("\n")
    file.close()
    return 0


def test_generateTabuSolution(testOutput, board, width, height):
    file = open(testOutput, "a")
    file.write("\n")
    file.write("\n")
    file.write("Tabu Solution Time: "+"\n")
    file.close()
    number = 0
    cleanboard = board.copy()
    whole_time = time.time()  # when alghoritm stats working
    while number < 25:
        single_try = time.time()  # when alghoritm stats working
        correctBoard = generateTabuSolution(board, width, height)
        single_try_time = time.time() - single_try
        number += 1
        board = cleanboard
        file = open(testOutput, "a")
        file.write("Time " + str(number) + ": " + str(single_try_time) + "\n")
        file.close()

    tabu_time = time.time() - whole_time
    file = open(testOutput, "a")
    file.write("Tabu Whole Time: " + str(tabu_time) + "\n")
    # file.write("Answer: " + str(correctBoard))
    file.write("\n")
    file.close()
    return 0


def main():
    filename = "1.txt"
    mapOutput = "output.txt"
    testOutput = "test_output.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        mapOutput = sys.argv[2]

    mapName = mapsFolder + filename
    cleanBoard = extractMap(mapName)  # empty map
    board = cleanBoard.copy()  # map we operate on
    width = getMapSizes(mapName)[0]
    height = getMapSizes(mapName)[1]

    start_time = time.time()  # when alghoritm stats working
    # correctBoard = bruteForce(board, width, height)
    # correctBoard = generateSimmannealingSolution(board, width, height)
    correctBoard = generateGeneticSolution(board, width, height, population_size=40, best_population_percentage=0.25, generations_number=1000, mutation_chance=0.1)
    work_time = time.time() - start_time
    board = cleanBoard.copy()

    printSolution(cleanBoard, correctBoard, width, height)
    print()
    print("Elapsed alghoritm work time : " + str(work_time))
    print()

    saveSolution(cleanBoard, correctBoard, width, height, work_time, mapOutput)
    # visuals.printFancyMap(cleanBoard, correctBoard, width, height)

    # print("Brute Force :")
    # print(correctBoard)  #bruteforce
    #
    # print("Random Guess Solution :")
    # board = cleanBoard.copy()  # map we operate on
    # randomGuessSolution = generateRandomSolution(board, width, height)
    # print(randomGuessSolution)
    #
    # print("Tabu Solution :")
    # board = cleanBoard.copy()  # map we operate on
    # tabuSolution = generateTabuSolution(board, width, height)
    # print(tabuSolution)
    #
    # print("Climbing Solution :")
    # board = cleanBoard.copy()  # map we operate on
    # climbingSolution = generateClimbingSolution(board, width, height)
    # print(climbingSolution)
    #
    # print("Random ONE Guess :")
    # board = cleanBoard.copy()  # map we operate on
    # print(randomiseMap(board, width, height))
    # TESTING
    # test_bruteForce(testOutput, board, width, height)
    # test_generateClimbingSolution(testOutput, board, width, height)
    # test_generateTabuSolution(testOutput, board, width, height)


if __name__ == "__main__":
    main()
