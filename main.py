import visuals
import time
import sys
import auxiliary
from algorithms import bruteforce, randomsolution, climbingv1, climbingv2, tabu, annealing, genetic

mapsFolder = "maps/"  # folder with maps to read from


def main():
    filename = "1.txt"
    mapOutput = "output.txt"
    testOutput = "test_output.txt"

    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        mapOutput = sys.argv[2]

    mapName = mapsFolder + filename
    cleanBoard = auxiliary.extractMap(mapName)  # empty map
    board = cleanBoard.copy()  # map we operate on
    height = auxiliary.getMapSizes(mapName)[0]
    width = auxiliary.getMapSizes(mapName)[1]

    start_time = time.time()  # when algorithm stats working
    # correctBoard = bruteforce.bruteForce(board, width, height)
    # correctBoard = climbingv1.generateClimbingSolution(board, width, height)
    # correctBoard = climbingv2.generateClimbingSolutionv2(board, width, height)
    # correctBoard = tabu.generateTabuSolution(board, width, height)
    # correctBoard = randomsolution.generateRandomSolution(board, width, height)
    # correctBoard = annealing.generateAnnealingSolution(board, width, height)
    correctBoard = genetic.generateGeneticSolution(board, width, height, population_size=100, best_population_percentage=10, generations_number=10000, mutation_chance=5)
    work_time = time.time() - start_time
    board = cleanBoard.copy()

    auxiliary.printSolution(cleanBoard, correctBoard, width, height)
    print()
    print("Elapsed alghoritm work time : " + str(work_time))
    print()

    auxiliary.saveSolution(cleanBoard, correctBoard, width, height, work_time, mapOutput)
    visuals.print_visuals(cleanBoard, correctBoard, width, height)

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
    # print(randomiseMap(board))
    # TESTING
    # test_bruteForce(testOutput, board, width, height)
    # test_generateClimbingSolution(testOutput, board, width, height)
    # test_generateTabuSolution(testOutput, board, width, height)


if __name__ == "__main__":
    main()
