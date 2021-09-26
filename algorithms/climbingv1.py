import rules


def generateClimbingSolution(board, width, height):
    errors = rules.checkQuality(board, width, height)
    while errors != 0:
        cleanBoard = board.copy()
        best_neighbour = []
        quality = 99  # error.txt indicator
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
        if neighbour_quality < errors:
            errors = neighbour_quality
            board = best_neighbour.copy()
        elif neighbour_quality >= errors:
            board = best_neighbour.copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
    return board
