import random
import rules


# Random algorithm works as a blind shoot for an answer:
# Good site is that it will find the correct answer,
# Bad site is that the process of finding the answer is completely random so it can take only a little time with is good
# but it can also technically take much more time than bruteforce because fo the random factor in it.


def generateRandomSolution(board, width, height):
    errors = rules.checkQuality(board, width, height)  # check number of errors
    while errors != 0:
        for i in range(0, len(board)):
            if board[i] == 0 or board[i] == 1:  # random roll if it will change
                board[i] = random.randint(0, 1)
        errors = rules.checkQuality(board, width, height)  # check the generated map on number of errors
    return board
