import random
import math
import rules


# Annealing algorithm :
# Good site is that ,
# Bad site is that .


def generateAnnealingSolution(board, width, height):
    temperature_formula = lambda temp: temperature * 0.9999
    # iterations = 100000
    temperature = 100
    board = board.copy()
    all_neighbors = []

    while True:
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
        all_neighbors = []
        cost_diff = rules.checkQuality(board, width, height) - rules.checkQuality(neighbor, width, height)

        if rules.checkQuality(board, width, height) == 0:
            # print(temperature)
            return board
        elif rules.checkQuality(neighbor, width, height) == 0:
            # print(temperature)
            return neighbor

        if cost_diff > 0:
            board = neighbor.copy()
        elif random.uniform(0, 1) < math.exp(cost_diff / temperature):
            board = neighbor.copy()
        temperature = temperature_formula(temperature)
        # print(temperature)
    #
    # print("ERROR: The algorithm is stuck and the last solution is: ")
    # errors = rules.checkQuality(board, width, height)
    # print("Errors number: " + str(errors))
    # return board


def generateAnnealingSolution1(board, width, height):
    temperature_formula = lambda temp: 1 / iterations  # wzór na tempoeraturę
    iterations = 10000
    temperature = 100
    # board = board.copy()
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
            print(all_neighbors)
        neighbor = random.choice(all_neighbors)
