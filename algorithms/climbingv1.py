import rules


# Climbing algorithm works as a find better solution than the staring one then go there:
# Good site is that it is fast, and it goes consistent to the answer,
# Bad site is that it can get stuck because if it finds a solution that is close to an answer but the next step is not
# the answer if can not go back because it only goes forward,
# It can get stuck in a local maximum.


def generateClimbingSolution(board, width, height):
    errors = rules.checkQuality(board, width, height)  # check how many errors we got on the starting map
    while errors != 0:
        cleanBoard = board.copy()  # save the empty map
        best_neighbour = []
        quality = 99  # error indicator
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = 1
                if quality > rules.checkQuality(board, width, height):
                    best_neighbour = board.copy()
            elif board[i] == 1:
                board[i] = 0
                if quality > rules.checkQuality(board, width, height):
                    best_neighbour = board.copy()
            board = cleanBoard.copy()
            quality = rules.checkQuality(board , width, height)
        neighbour_quality = rules.checkQuality(best_neighbour, width, height)

        if len(best_neighbour) == 0:
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
        elif neighbour_quality < errors:
            errors = neighbour_quality
            board = best_neighbour.copy()
        elif neighbour_quality == errors:
            errors = neighbour_quality
            board = best_neighbour.copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
        else:
            board = board.copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
    return board
