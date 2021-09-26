import rules


def generateTabuSolution(board, width, height):
    tabu_list = [board]
    errors = rules.checkQuality(board, width, height)
    while errors != 0:
        cleanBoard = board.copy()
        best_neighbour = []
        quality = 99  # error.txt indicator
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = 1
                if quality > rules.checkQuality(board, width, height) and not tabu_list.__contains__(board):
                    best_neighbour = board.copy()
            elif board[i] == 1:
                board[i] = 0
                if quality > rules.checkQuality(board, width, height) and not tabu_list.__contains__(board):
                    best_neighbour = board.copy()
            board = cleanBoard.copy()

        if not best_neighbour:  # if best_neighbour is empty -> all neighbours are tabu
            print("ERROR: The algorithm is stuck and the last solution is: ")
            errors = rules.checkQuality(board, width, height)
            print("Errors number: " + str(errors))
            return board
        tabu_list.append(best_neighbour)
        board = best_neighbour.copy()
        errors = rules.checkQuality(board, width, height)
    return board
