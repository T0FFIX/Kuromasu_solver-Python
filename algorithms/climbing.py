import rules


# Climbing algorithm works as a find better solution than the previous one then go there:
# Good site is that it is fast, and it goes consistent to the answer,
# Bad site is that it can get stuck because if it finds a solution that is close to an answer but the next step is not
# it can not go back and is looks for the best answer in the radius of one step so it can get stuck in a local maximum.


def generateClimbingSolution(board, width, height):
    i = 0  # initialize i iterator
    best_neighbour = board.copy()  # save the map as the best current
    quality = rules.checkQuality(board, width, height)  # check current quality
    while i < len(board):
        if board[i] == 0:  # if the cell is while
            board[i] = 1  # change to black
        elif board[i] == 1:  # if the cell is black
            board[i] = 0  # change to while

        if rules.checkQuality(board, width, height) < quality:  # the quality is better then before
            quality = rules.checkQuality(board, width, height)  # override quality
            best_neighbour = board.copy()  # we got our potential best neighbour
            i = 0  # reset i iterator to check the map from start again
        else:
            board = best_neighbour.copy()  # reset map to best neighbour (to its best previous state)
            i += 1  # increment i

    if rules.checkQuality(best_neighbour, width, height) > 0:  # check if there are some errors
        # algorithm got stuck and the answer is not entirely correct
        quality = rules.checkQuality(best_neighbour, width, height)  # get number of errors
        print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(quality))
    return best_neighbour
