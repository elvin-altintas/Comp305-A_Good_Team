## A Good Team - Room 28 Term Project
## Elvin Altintas, Irem Zeynep Dundar, Kutluhan Palalioglu, Simay Ozdemir
## Efforts in this below implementation belongs to all of the group members.


## Neighbor number of each spot on the board can be calculated via neighbor_count(i, j, arr)
## Cornes, edges and middle spots are evaluated differently
def neighbor_count(i,j,arr):
  neighbor = 0

  if j == 0 : #leftmost column

    if i == 0: #upper left corner

      if (i,j+1) in assigned: 
        neighbor+=1
      if (i+1, j) in assigned:
        neighbor+= 1

    elif i == len(arr)-1: #lower left corner

      if (i-1, j) in assigned: 
        neighbor += 1
      if (i, j+1) in assigned: 
        neighbor += 1

    else: #leftmost column, middle spots

      if (i-1, j) in assigned: 
        neighbor += 1
      if (i+1, j) in assigned: 
        neighbor += 1
      if (i, j + 1) in assigned:
        neighbor += 1
  elif j == len(arr[0])-1: #rightmost column

    if i == 0: #upper right corner

      if (i, j - 1) in assigned:  
        neighbor += 1

      if (i + 1, j) in assigned: 
        neighbor += 1


    elif i == len(arr) - 1: #lower right corner

      if (i - 1, j) in assigned:  
        neighbor += 1
      if (i, j - 1) in assigned: 
        neighbor += 1

    else: #rightmost column, middle spots

      if (i - 1, j) in assigned:  
        neighbor += 1
      if (i, j - 1) in assigned:  
        neighbor += 1
      if (i+1, j) in assigned: 
        neighbor += 1
  elif i == 0: #uppermost line, middle spots

    if (i, j+1) in assigned:  
      neighbor += 1
    if (i, j - 1) in assigned:  
      neighbor += 1
    if (i+1, j) in assigned: 
      neighbor += 1
  elif i == len(arr)-1: #lowermost line, middle spots

    if (i, j+1) in assigned:  
      neighbor += 1
    if (i, j - 1) in assigned:  
      neighbor += 1
    if (i-1, j) in assigned: 
      neighbor += 1
  else: #middle spots

    if (i, j+1) in assigned:
      neighbor += 1
    if (i, j - 1) in assigned: 
      neighbor += 1
    if (i-1, j) in assigned: 
      neighbor += 1
    if (i+1, j) in assigned: 
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

assigned = {} # assigned spot list
available = {} # available spot list

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
      if arr[i][j] == ".": # no spot is available
        if (i + j) % 2 == 1:
          nv2 += 1
        else:
          nv1 += 1


      elif arr[i][j] == "#": # pre assigned spot
        if (i + j) % 2 == 1:
          v2 += 1
        else:
          v1 += 1
        assigned[(i,j)] = 0

      elif arr[i][j] == "?": # available as spot
        available[(i,j)] = 0

  if v1-nv1 > v2-nv2 :
    version = 1
  else:
    version = 2
  print("Winner version: ", version)
  print("version1: ", v1)
  print("version2: ", v2)
  print("negatve version1: ", nv1)
  print("negative version2: ", nv2)
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

  # print("Preassigned:",assigned)
  # print("Beginning | Available:",available)


  # Step 1
  print("Test for STEP 1")
  temp_available1 =  available.copy()
  print("Available", temp_available1)
  print("Assigned", assigned)
  for index in temp_available1.keys():
    print("index",index)
    i = index[0]
    j = index[1]
    n_count = neighbor_count(i, j, arr)
    print("neighbour count", n_count)
    if (i + j)%2  == remainder and n_count == 0:

      assigned[(i,j)] = 4
      available.pop((i,j))

  print("Total Assigned in Step 1")
  visualize(assigned, arr)

  # Step 2
  print("\n\n")
  print("Test for STEP 2")
  print("Available", temp_available1)
  print("Assigned", assigned)
  temp_available2 =  available.copy()
  for index in temp_available2.keys():
    i = index[0]
    j = index[1]
    n_count = neighbor_count(i, j, arr)
    if n_count == 0 or n_count == 1 :

      assigned[(i, j)] = 4
      available.pop((i, j))
      

  print("Total Assigned in Step 2")
  visualize(assigned, arr)
  # print("Step 2 | Available:", available)
  # print("Step 2 | Assigned: ", assigned)

  # calculating each spots score
  for index  in assigned.keys():
    i = index[0]
    j = index[1]
    n_count = neighbor_count(i, j, arr)
    assigned[(i, j)] = 4-n_count
    score += assigned[(i, j)]

  visualize(assigned, arr)

  return score

## In order to visualize the board for debugging
def visualize(assigned, arr):

  print("TEST in VISUALIZE")
  # init res table
  res = [[0] * len(arr[0])]*len(arr)

  score = 0
  # fill res table
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if (i,j) in assigned.keys():
        print("(i,j): ", i,j)
        print("Assigned (i,j) score", assigned[(i,j)])
        print()
        score += assigned[(i,j)]
        res[i][j] = assigned[(i,j)]
  print("score:", score)

  # print table
  line = ""
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      line = line +" "+ str(res[i][j])
    line = line + "\n"

  print(line)

if __name__ == "__main__":

  test1 =  [".?.",".?.",".#."]
  out1 =["",]
  test2 = [".#...##.",
           ".##..?..",
           ".###.#.#",
           "??#..?..",
           "###?#..." ]

  #.#...##. .##..?.. .###.#.# ??#..?.. ###?#...

  print("Score ", a_good_team(test2))

  # test_case = int(input())
  # for _ in range(test_case):
  #   arr = read_inputs()
  #   print(arr)
  #   print("Score ",a_good_team(arr))
  # print("exit")
