import ball_sort_main as problem
import utils
import ucs
import time


# Input Statement with Text
#The input is always correct, no need to validate or check
#row1 = input("First Row: ").split(" ")
#row2 = input("Second Row: ").split(" ")
#row3 = input("Third Row: ").split(" ")
#row4 = input("Forth Row: ").split(" ")

row1 = input("").split(" ")
row2 = input("").split(" ")
row3 = input("").split(" ")
row4 = input("").split(" ")

start = time.time()

#Input Management
#Columns 
listc1 = []
listc1.append(row4[0])
listc1.append(row3[0])
listc1.append(row2[0])
listc1.append(row1[0])

problem.start_input[0] = listc1

listc2 = []

listc2.append(row4[1])
listc2.append(row3[1])
listc2.append(row2[1])
listc2.append(row1[1])

problem.start_input[1] = listc2

listc3 = []

listc3.append(row4[2])
listc3.append(row3[2])
listc3.append(row2[2])
listc3.append(row1[2])

problem.start_input[2] = listc3

listc4 = []

listc4.append(row4[3])
listc4.append(row3[3])
listc4.append(row2[3])
listc4.append(row1[3])

problem.start_input[3] = listc4

#Empty Stacks
listc5 = [] 
problem.start_input[4] = listc5
listc6 = []
problem.start_input[5] = listc6

#problem.print_step(0)

goal_node, n_visits = ucs.uniform_cost_graph_search(problem)
if goal_node is not None:
    
    utils.print_solution(goal_node)
    #problem.print_step(goal_node[0], 0)
    
    #print("Path cost = %d" % goal_node[3])
    #print("Number of Visited States = %d" % n_visits)

else:
    print("No solutions found")
#print("Time Taken: %.2f seconds" %(time.time() - start))

#----------------------------------------------------------------------------------------------------------------
#ballsortproblem.uniform_cost_graph_search(listc1, listc2, listc3, listc4, listc5, #listc6)

#Checking statement
#----------------------------------------------------------------------------------------------------------------
#print(listr1 + " \n" + listr2 + " \n" + listr3 + " \n" + listr4)
#ballsortproblem.uniform_cost_graph_search()
#----------------------------------------------------------------------------------------------------------------