## A Good Team - Room 28 Term Project
## Elvin Altıntaş, İrem Zeynep Dündar, Kutluhan Palalıoğlu, Simay Özdemir

## Neighbor number of each spot on the board can be calculated via neighbor_count(i, j, arr)
## Cornes, edges and middle spots are evaluated differently
def neighbor_count(i, j, arr):
    neighbor = 0

    if j == 0:

        if i == 0:

            if (i, j + 1) in assigned:  # right
                neighbor += 1
            if (i + 1, j) in assigned:  # down
                neighbor += 1

        elif i == len(arr) - 1:  # (n-1,1),(n-2,0)

            if (i - 1, j) in assigned:  # up
                neighbor += 1
            if (i, j + 1) in assigned:  # right
                neighbor += 1

        else:  # (i-1, j), (i+1,j), (i,j+1)

            if (i - 1, j) in assigned:  # ust
                neighbor += 1
            if (i + 1, j) in assigned:  # alt
                neighbor += 1
            if (i, j + 1) in assigned:  # sag
                neighbor += 1
    elif j == len(arr[0]) - 1:

        if i == 0:

            if (i, j - 1) in assigned:  # sol
                neighbor += 1

            if (i + 1, j) in assigned:  # alt
                neighbor += 1


        elif i == len(arr) - 1:

            if (i - 1, j) in assigned:  # ust
                neighbor += 1
            if (i, j - 1) in assigned:  # sol
                neighbor += 1

        else:

            if (i - 1, j) in assigned:  # up
                neighbor += 1
            if (i, j - 1) in assigned:  # left
                neighbor += 1
            if (i + 1, j) in assigned:  # down
                neighbor += 1
    elif i == 0:

        if (i, j + 1) in assigned:  # right
            neighbor += 1
        if (i, j - 1) in assigned:  # left
            neighbor += 1
        if (i + 1, j) in assigned:  # down
            neighbor += 1
    elif i == len(arr) - 1:

        if (i, j + 1) in assigned:  # right
            neighbor += 1
        if (i, j - 1) in assigned:  # left
            neighbor += 1
        if (i - 1, j) in assigned:  # up
            neighbor += 1
    else:

        if (i, j + 1) in assigned:  # right
            neighbor += 1
        if (i, j - 1) in assigned:  # left
            neighbor += 1
        if (i - 1, j) in assigned:  # up
            neighbor += 1
        if (i + 1, j) in assigned:  # down
            neighbor += 1

    return neighbor

## Takes the input: test case number, height and width of the board, assignments of spots
def read_inputs():
    hw = input()
    h = int(hw.split()[0])
    w = int(hw.split()[1])
    arr = list()

    for k in range(h):
        line = input()
        arr.append(line)
    return arr


assigned = {}  # spot list
available = {}  # available for spots

## This function checks the pre-assigned spots to determine which checkerboard format is the most suitable
## Pre-assigned spots belonging to a specific version increases the score of that version, 
## unavailable spots belonging to a specific version decreases the score of that version.
## Returns the most suitable chekerboard version
def format_board(arr):
    v1 = 0
    v2 = 0

    nv1 = 0
    nv2 = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == ".":  # no spot is available
                if (i + j) % 2 == 1:
                    nv2 += 1
                else:
                    nv1 += 1


            elif arr[i][j] == "#":  # pre assigned spot
                if (i + j) % 2 == 1:
                    v2 += 1
                else:
                    v1 += 1
                assigned[(i, j)] = 0

            elif arr[i][j] == "?":  # available as spot
                available[(i, j)] = 0

    if v1 - nv1 > v2 - nv2:
        version = 1
    else:
        version = 2

    return version

## Implements step 1 and 2
## Fills the available spots fitting the checkerboard version which has no neighbors (Step 1)
## Fills the available spots having 0 or 1 neighbors (Step 2)
## Returns the score of the board
def a_good_team(arr):
    score = 0
    version = format_board(arr)

    if version == 1:
        remainder = 0
    else:
        remainder = 1

    # step 1

    temp_available1 = available.copy()
    for index in temp_available1.keys():
        i = index[0]
        j = index[1]
        n_count = neighbor_count(i, j, arr)
        if (i + j) % 2 == remainder and n_count == 0:
            assigned[(i, j)] = 4
            available.pop((i, j))

    temp_available2 = available.copy()
    for index in temp_available2.keys():
        i = index[0]
        j = index[1]
        n_count = neighbor_count(i, j, arr)
        if n_count == 0 or n_count == 1:
            assigned[(i, j)] = 4
            available.pop((i, j))

    # calculating each spots score
    for index in assigned.keys():
        i = index[0]
        j = index[1]
        n_count = neighbor_count(i, j, arr)
        assigned[(i, j)] = 4 - n_count
        score += assigned[(i, j)]

    assigned.clear()
    available.clear()
    return score


if __name__ == "__main__":
    # given test example
    # 2
    # 3 3
    # .?.
    # .?.
    # .#.
    # 5 8
    # .#...##.
    # .##..?..
    # .###.#.#
    # ??#..?..
    # ###?#...

    # extra test case 1
# 2
# 7
# 5
# # ???.
# ??  # ?#
# ?????
# .?..?
# ?  # ?#?
# ????.
# .?  # .?
# 6 5
# ??#?#
# ?????
# .?..?
# ?#?#?
# ????.
# .?#.?

    # extra test case 2
    # 2
    # 6
    # 4
    # # ???
    # .  # .?
    # ??  ##
    # ????
    # ????
    # ?  # ?.
    # 12
    # 3
    # .?.
    # ??  #
    # ??.
    # ???
    # ???
    # ?  # ?
    # .??
    # # ?.
    # ??  #
    # ???
    # ?  ##
    # ?  ##

    # test = [".?.",
    #         "??#",
    #         "??.",
    #         "???",
    #         "# ???",
    #         "?#?",
    #         ".??",
    #         "#?.",
    #         "??#",
    #         "???",
    #         "?##",
    #         "?##",]
    # print(a_good_team(test))

    test_case = int(input())
    test_list=list()

    for i in range(test_case):
       test_list.append(read_inputs())
    print("Outputs:\n")
    for test in test_list:
        print("Score ",a_good_team(test))
