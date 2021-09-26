import time
import main


def test_bruteForce(testOutput, board, width, height):
    file = open(testOutput, "w")
    file.close()
    file = open(testOutput, "a")
    file.write("Brute Force Solution Time: " + "\n")
    file.close()
    number = 0
    cleanboard = board.copy()
    whole_time = time.time()  # when algorithm stats working
    while number < 25:
        single_try = time.time()  # when algorithm stats working
        correctBoard = main.bruteForce(board, width, height)
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
        correctBoard = main.generateClimbingSolution(board, width, height)
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
    whole_time = time.time()  # when algorithm stats working
    while number < 25:
        single_try = time.time()  # when algorithm stats working
        correctBoard = main.generateTabuSolution(board, width, height)
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