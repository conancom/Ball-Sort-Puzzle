from heapq import heappush, heappop, heapify
from utils import create_node
from utils import print_step
'''
def uniform_cost_tree_search(problem):
    initial_node = create_node(problem.initial_state(), None, "", 0, 0)
    frontier = [(0, initial_node)] #0 represents Path cost
    n_visits = 0
    while True:
        if not frontier: #If frontier is empty, means we searched everything with no goal state or no solution
            return (None, n_visits)
        else:#Frontier contains something
            n_visits += 1#Keep track of nodes we visited
            _, node = heappop(frontier)#Removes the node with min cost
            state, _, _, path_cost, depth = node
            if problem.is_goal(state):#Check if it is the goal
                return (node, n_visits)#Found solution
            else: # Not goal state 
                for succ, cost in problem.successors(state):# Generate successors
                    child_cost = path_cost + cost
                    child = create_node(succ, node, "", child_cost,
                                        depth + 1)
                    heappush(frontier, (child_cost, child))#Will be inputed into heap to run in the next iteration
'''

def index(f, s):#f is frontier(list) s is state 
    return next((i for i, x in enumerate(f) if x[1][0] == s), -1)# returns index of s in f, returns -1 if not found


def uniform_cost_graph_search(problem):
    initial_node = create_node(problem.initial_state(), None, "", 0, 0)
    frontier = [(0, initial_node)] #Frontier = Where we keep all the successor state
    explored = set() #Creation of unordered collection data type that is iterable
    n_visits = 0 #Starting so no visits just yet
    step = 0 #No Steps
    while True:
        #print_step(frontier, n_visits)
        if not frontier: 
            return (None, n_visits)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, _, _, path_cost, depth = node
            #print_step(state, path_cost)
            explored.add(tuple(map(tuple, state))) # Can't input list -> Tried tuple didnt work #The only modified part 
            if problem.is_goal(state, n_visits-1): # n_visits-1 used to print out step
                return (node, n_visits)
            else:
                for succ, cost in problem.successors(state, n_visits):#printing out step
                    child_cost = path_cost + cost #Increasing path cost if chosen the next node
                    child = create_node(succ, node, "", child_cost, depth + 1) #Create the successor
                    if (tuple(map(tuple, succ))) not in explored:# Check if it is not explored (new state) -> Explored meaning if the algorithm ran through it to avoid        A-> B -> A
                        idx = index(frontier, succ)
                        if idx < 0:#Successor is not in frontier
                            heappush(frontier, (child_cost, child))
                            
                            #step +=1 
                        else:#Successor is in frontier , make sure only the smallest version of the node is in the frontier
                            _, existing = frontier[idx]
                            if existing[3] > child_cost:#Smaller cost -> Replace expensive with the cheaper version
                                frontier[idx] = (child_cost, child)
                                heapify(frontier)

                
                                
                                
        
