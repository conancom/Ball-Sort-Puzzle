start_input = [[],[],[],[],[],[]]


def print_step(step):
  print("Step " + str(step))
  #Stack Creations with the checking conditions for ones with dot
  for i in range(3,-1,-1):
    try: 
      print(start_input[0][i], end = ' ')
    except:
      print(".", end = ' ')
  
    try:
      print(start_input[1][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(start_input[2][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(start_input[3][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(start_input[4][i], end = ' ')
    except:
      print(".", end = ' ')

    try:
      print(start_input[5][i], end = ' ')
    except:
      print(".")

def initial_state():
  return start_input

def successors(s):
  for i in range(5,-1,-1):
    if len(start_input[i]) != 0:
      for j in range(5,-1,-1):
        if start_input[i][len(start_input[i])-1] == start_input[j][len(start_input[j])-1] or len(start_input[j]) == 0 and  i != j and len(start_input[j]) != 4:
          start_input[j].append(start_input[i].pop())
          return start_input




  for e in start_input:
    if e[0] == s:
      yield e[1], e[2]
    elif e[1] == s:
      yield e[0], e[2]

def is_goal(s): #If the code is wrong, it is this part is the reason
    return check_column(s[0]) and check_column(s[1]) and check_column(s[2]) and check_column(s[3]) and check_column(s[4]) and check_column(s[5]) 

def check_column(column):
  if len(column) == 0:
    return False
  if all(x == check_column[0] for x in check_column[0]):
    return True
  else:
    return False

