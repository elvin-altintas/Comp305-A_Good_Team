	## A Good Team - Room 28 Term Project
## Elvin Altıntaş, İrem Zeynep Dündar, Kutluhan Palalıoğlu, Simay Özdemir

## Neighbor number of each spot on the board can be calculated via neighbor_count(i, j, arr)
## Cornes, edges and middle spots are evaluated differently
import time


def read_sample_output():
  sample_output = {}
  file1 = open("small-testdata.out", "r+")
  txt = file1.read()
  output = txt.split("\n")

  for k in range(len(output) - 1):
    out = output[k].split(":")[1]
    sample_output[k] = int(out[1:len(out)])
  return sample_output


def read_sample_input():
  sample_test_cases = {}
  file1 = open("small-testdata.in", "r+")
  txt = file1.read()
  txt_split = txt.split("\n")
  total_test_case_no = int(txt_split[0])  # txt[0:len(txt[0])]
  test_case_data = txt_split[1:len(txt_split)]

  i = 0
  for k in range(total_test_case_no):
    rc = test_case_data[i].split()
    r, c = int(rc[0]), int(rc[1])
    sample_test_cases[k] = test_case_data[i + 1: i + 1 + r]
    i = r + i + 1
  return sample_test_cases


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

          if (i - 1, j) in assigned:  # up
              neighbor += 1
          if (i + 1, j) in assigned:  # down
              neighbor += 1
          if (i, j + 1) in assigned:  # right
              neighbor += 1
  elif j == len(arr[0]) - 1:

      if i == 0:

          if (i, j - 1) in assigned:  # left
              neighbor += 1

          if (i + 1, j) in assigned:  # down
              neighbor += 1


      elif i == len(arr) - 1:

          if (i - 1, j) in assigned:  # up
              neighbor += 1
          if (i, j - 1) in assigned:  # left
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
    # 7 5
    # #???.
    # ??#?#
    # ?????
    # .?..?
    # ?#?#?
    # ????.
    # .?#.?
    # 6 5
    # ??#?#
    # ?????
    # .?..?
    # ?#?#?
    # ????.
    # .?#.?

    # extra test case 2
    # 2
    # 6 4
    # #???
    # .#.?
    # ??##
    # ????
    # ????
    # ?#?.
    # 12 3
    # .?.
    # ??#
    # ??.
    # ???
    # ???
    # ?#?
    # .??
    # #?.
    # ??#
    # ???
    # ?##
    # ?##

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
    # test_case = int(input())
    # test_list=list()
    #
    # for i in range(test_case):
    #    test_list.append(read_inputs())
    # start = time.time()
    #
    # for test in test_list:
    #    print("Score: ",a_good_team(test))
    #    end = time.time()
    #    print("Runtime for custom cases: ", end - start)

    ## default test cases
    start = time.time()
    corr = 0
    sample_test_cases = read_sample_input()
    sample_test_outputs = read_sample_output()

    for t in range(len(sample_test_cases.keys())):
      print()
      print("Test case t:", t)
      print("Algorithm Score:", a_good_team(sample_test_cases[t]), " | ",
            "Real Score:", sample_test_outputs[t])
      if sample_test_outputs[t] == a_good_team(sample_test_cases[t]):
        corr += 1
      end = time.time()
      print("Runtime for default cases: ", end - start)
      print()

    print("Accuracy of the algorithm: ", corr / 100)


