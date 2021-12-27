from collections import deque


def create_node(state, parent, action, path_cost, depth):
    return (tuple(state), parent, action, path_cost, depth) # Tuple of 5 elements


def print_solution(n):#Takes in Node n, traces backward from n to the initial state
    r = deque() #Double -end queue (Add and remove data at both ends)
    while n is not None:
        r.appendleft(n[0])#n[0] => State (First member of tuple)
        n = n[1]  #n[1] => Parent
    count = 0
    for s in r:
        print_step(s, count)
        print()
        count+=1

def print_step(state, step):  #State contains all the possible States of original
  print("Step " + str(step))
  #Stack Creations with the checking conditions for ones with dot
  for i in range(3,-1,-1):
    try: 
      print(state[0][i], end = ' ')
    except:
      print(".", end = ' ')
  
    try:
      print(state[1][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(state[2][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(state[3][i], end = ' ')
    except: 
      print(".", end = ' ')

    try:
      print(state[4][i], end = ' ')
    except:
      print(".", end = ' ')

    try:
      print(state[5][i])
    except:
      print(".")