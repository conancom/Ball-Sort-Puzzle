start_input = [[],[],[],[],[],[]]
from copy import deepcopy

#----------------------------------------------------------------------------------------------------------------

def print_step(state, step): #Outputs every steps
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

#----------------------------------------------------------------------------------------------------------------

def initial_state():
  return start_input

#----------------------------------------------------------------------------------------------------------------

def successors(s, cur_step):
  #print_step(s, cur_step) #Print Step before the nodes, s = state
  for i in range(5,-1,-1): #6 Stacks, Column
    succ_state = deepcopy(s) #Make a copy of 2D array
    if len(succ_state[i]) >= 1:
      for j in range(5,-1,-1): #6 Stacks, Row
        if len(succ_state[j]) > 0: # [len(succ_state[i])-1 => -1 wouldnt exist
          if succ_state[i][len(succ_state[i])-1] == succ_state[j][len(succ_state[j])-1] and  i != j and len(succ_state[j]) < 4 : #and not check_column(start_input[i])
            succ_state2 = deepcopy(succ_state)
            succ_state2[j].append(succ_state2[i].pop())
            yield succ_state2, 1
        else:
          if i != j:
            succ_state2 = deepcopy(succ_state)
            succ_state2[j].append(succ_state2[i].pop())
            yield succ_state2, 1
      #break
      
#----------------------------------------------------------------------------------------------------------------

def is_goal(s, cur_step): #If the code is wrong, it is this part is the reason
  answer = [False, False, False, False, False, False]  
  
  for i in range(5,-1,-1):

    if len(s[i]) == 4 :
      answer[i] = check_column(s[i])
    elif len(s[i]) == 0:
      answer[i] = True
    else:
      answer[i] = False
  
  return all(answer) #Takes logical AND of whole array

#----------------------------------------------------------------------------------------------------------------

  #return check_column(s[0]) and len(s[0]) == 4 and check_column(s[1]) and len(s[1]) == 4 and check_column(s[2]) and len(s[2])  == 4 and #check_column(s[3]) and len(s[3])  == 4 and check_column(s[4]) and len(s[4])  == 4 and len(s[5])  == 4 and check_column(s[5]) 
    
def check_column(column): #Always the last one being false for some reason
  if len(column) == 0:
    return False
  return len(set(column)) == 1 

#----------------------------------------------------------------------------------------------------------------