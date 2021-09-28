import rules


# Brute force algorithm works as a check all possible answers:
# Good site of it is that it always finds a answer even if it takes a loot of time,
# Bad site is that the time needed to find the solution is increased dramatically and is dependent on the complexity,
# in simple words the bigger the problem the more time it takes and therefore its much slower than others algorithms.


def appendWithZeros(element, size):
    new = ""
    for i in range(0, size - len(element)):  # generate the number of zeros that is needed
        new += str(0)

    new += element  # add those zeros in front to the generated binary number
    return list(new)


def insertNumbers(board, cleanBoard):
    for i in range(len(cleanBoard)):
        if int(cleanBoard[i]) >= 2:  # if the empty map has a number on the cell
            board[i] = cleanBoard[i]  # overwrite this number on the generated map
    return board


def bruteForce(cleanBoard, width, height):
    for i in range(0, 2 ** len(cleanBoard)):  # it takes to find an answer 2 ^ map size
        board = []
        generated = str(bin(i))  # refactor a decimal number (i) to binary
        # simply when you think about it, you can use the binary number as a generator of all possible outcomes

        generated = appendWithZeros(generated[2:], len(cleanBoard))  # add the missing zeros at the start
        # E.g. 10 = in binary 1010 then append the missing zeros map is 16 cells: 0000 0000 0000 1010

        for letter in generated:
            board.append(int(letter))  # add the generated numbers to board as a map

        board = insertNumbers(board, cleanBoard)  # insert the numbers on the generated map

        if rules.checkQuality(board, width, height) == 0:  # check if it is correct
            return board
