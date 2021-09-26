import random
import rules


def generateGeneticSolution(board, width, height, population_size, best_population_percentage, generations_number, mutation_chance):
    population = generatePopulation(board, population_size)  # population of answers for the starting population
    repopulate_number = population_size - best_population_percentage  # how many answers we need to generate to repopulate

    # check starting population for an answer
    for el in population:
        if rules.checkQuality(el, width, height) == 0:
            return el

    for k in range(0, generations_number):
        best_population_percentage_groups = []
        for m in range(best_population_percentage):
            single_group = []
            for n in range(population_size//best_population_percentage):
                pick_random_one = random.randrange(0, len(population))
                single_group.append(population[pick_random_one])
            best_population_percentage_groups.append(single_group)

        best = []
        for m in range(best_population_percentage):
            local_best_quality = 999  # error indicator
            local_best = []
            for n in range(population_size//best_population_percentage):
                groups_one_instance = best_population_percentage_groups[m][n]
                groups_one_instance_quality = rules.checkQuality(groups_one_instance, width, height)
                if groups_one_instance_quality < local_best_quality:
                    local_best = groups_one_instance
                    local_best_quality = groups_one_instance_quality
            best.append(local_best)

        random_crossing_position = random.randrange(0, len(best)-1)

        dna_first_half = []
        dna_second_half = []
        for el in best:
            dna_first_half.append(el[0:random_crossing_position])
            dna_second_half.append(el[random_crossing_position:])

        new_generation = []
        for i in range(0, repopulate_number):
            random_choice_first_half = random.randrange(0, len(best))
            random_choice_second_half = random.randrange(0, len(best))

            offspring = dna_first_half[random_choice_first_half].copy()
            offspring.extend(dna_second_half[random_choice_second_half].copy())
            new_generation.append(offspring)

        for i in range(0, round(repopulate_number*mutation_chance)):
            mutated_offspring = random.randrange(0, len(new_generation))
            mutation = new_generation[mutated_offspring]
            mutated_position = random.randrange(0, len(mutation))

            while mutation[mutated_position] > 1:
                mutated_position = random.randrange(0, len(mutation))

            # switches from 0 to 1 and from 1 to 0
            if mutation[mutated_position] == 0:
                mutation[mutated_position] = 1
            else:
                mutation[mutated_position] = 0

        for el in best:
            new_generation.append(el)

        population = new_generation.copy()

        # check last generation for an answer
        for el in population:
            if rules.checkQuality(el, width, height) == 0:
                return el

    # even if we have no answer, return best possible from last generation
    population = sortByQuality(population, width, height)
    print("ERROR: The algorithm is stuck and the last solution from the last generation is: ")
    errors = rules.checkQuality(population[0], width, height)
    print("Errors number: " + str(errors))
    return population[0]


def generatePopulation(board, population_size):
    #   generates a random but unique population of answers
    population = []
    clean_board = board.copy()
    for j in range(0, population_size):
        for i in range(0, len(board)):
            if board[i] == 0 or board[i] == 1:
                board[i] = random.randint(0, 1)
        if not population.__contains__(board):
            population.append(board)
        board = clean_board.copy()

    return population


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
