def checkQuality(board, width, height):
    error = 0
    for i in range(0, len(board)):
        # Rule 1: Each number on the board represents the number of white cells that can be seen from that cell,
        # including itself. A cell can be seen from another cell if they are in the same row or column, and there
        # are no black cells between them in that row or column.
        if board[i] != 1 and board[i] != 0:  # in this cell is a number
            count = 1  # number of white cells, it automatically count itself at start
            iterator = 0

            # Check left side
            while True:
                iterator += 1
                if i % width - iterator >= 0 and board[i - iterator] != 1:
                    count += 1  # the next cell is white
                else:
                    break  # the next cell is not white
            # Reset
            iterator = 0
            # Check up side
            while True:
                iterator += 1
                if i - width * iterator >= 0 and board[i - width * iterator] != 1:
                    count += 1  # the next cell is white
                else:
                    break  # the next cell is not white
            # Reset
            iterator = 0
            # Check right side
            while True:
                iterator += 1
                if i % width + iterator < width and board[i + iterator] != 1:
                    count += 1  # the next cell is white
                else:
                    break  # the next cell is not white
            # Reset
            iterator = 0
            # Check down side
            while True:
                iterator += 1
                if i + width * iterator < width*height and board[i + width * iterator] != 1:
                    count += 1  # the next cell is white
                else:
                    break  # the next cell is not white
            # Check if the number inside the cell is equal to count if not its an error
            if board[i] != count:
                error += 1

        # Rule 2: No two black cells may be horizontally or vertically adjacent.
        if board[i] == 1:  # check self if on black cell
            if (i % width) + 1 < width and board[i + 1] == 1:  # check right side
                error += 1  # it is connected, add error

            elif i + width < width * height and board[i + width] == 1:  # check down side
                error += 1  # it is connected, add error

            elif (i % width) - 1 > 0 and board[i - 1] == 1:  # check left side
                error += 1  # it is connected, add error

            elif i - width > 0 and board[i - width] == 1:  # check up side
                error += 1  # it is connected, add error
            else:
                pass  # if no black cell is connected, continue

        # Rule 3: All the white cells must be connected horizontally or vertically.
        if board[i] == 0:
            # Reset to reuse this variable
            count = 0
            if (i % width) + 1 < width:
                if board[i + 1] == 0 or board[i + 1] > 1:  # check right side
                    pass
                else:
                    count += 1
            else:
                count += 1

            if i + width < width * height:
                if board[i + width] == 0 or board[i + width] > 1:  # check down side
                    pass
                else:
                    count += 1
            else:
                count += 1

            if (i % width) - 1 >= 0:
                if board[i - 1] == 0 or board[i -1] > 1:  # check left side
                    pass
                else:
                    count += 1
            else:
                count += 1

            if i - width >= 0:
                if board[i - width] == 0 or board[i - width] > 1:  # check up side
                    pass
                else:
                    count += 1
            else:
                count += 1

            if count == 4:  # the white cell is surrounded by black cells and/or edges of the map
                error += 1  # it is not connected to the others, add error
    return error