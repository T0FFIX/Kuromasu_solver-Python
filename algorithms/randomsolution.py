import random
import rules


def generateRandomSolution(board, width, height):
    errors = rules.checkQuality(board, width, height)
    while errors != 0:
        for i in range(0, len(board)):
            if board[i] == 0 or board[i] == 1:
                board[i] = random.randint(0, 1)
        errors = rules.checkQuality(board, width, height)
    return board