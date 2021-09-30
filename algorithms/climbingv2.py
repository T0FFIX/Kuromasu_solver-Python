import rules


def generateClimbingSolutionv2(board, width, height):
    errors = rules.checkQuality(board, width, height)
    while errors != 0:
        cleanBoard = board.copy()
        best_neighbour = []
        quality = 99  # error indicator
        for i in range(0, len(board)):
            if board[i] == 0:
                board[i] = 1
                if quality > rules.checkQuality(board, width, height):
                    best_neighbour.append(board)
            elif board[i] == 1:
                board[i] = 0
                if quality > rules.checkQuality(board, width, height):
                    best_neighbour.append(board)
            board = cleanBoard.copy()
        sorted_neighbours = []
        for i in range(0, len(best_neighbour)):
            sorted_neighbours = sortByQuality(best_neighbour, width, height)
        neighbour_quality = rules.checkQuality(sorted_neighbours[0], width, height)

        if neighbour_quality < errors:
            errors = neighbour_quality
            board = sorted_neighbours[0].copy()
        elif neighbour_quality == errors:
            errors = neighbour_quality
            board = sorted_neighbours[0].copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
        else:
            board = board.copy()
            print("ERROR: The algorithm is stuck and the last solution has so many errors: " + str(errors))
            break
    return board


def sortByQuality(population, width, height):
    #   sorts population by how many errors it hase and returns it
    population_qualities = []
    for el in population:
        dict_el = [el, rules.checkQuality(el, width, height)]
        population_qualities.append(dict_el)

    population_qualities = sorted(population_qualities, key=lambda x: x[1], reverse=False)

    population = []
    for el in population_qualities:
        population.append(el[0])
    return population
