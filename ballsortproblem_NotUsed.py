#Declartions of variables and lists
frontier = [] #The set of successors
visited = [] #Keep the visited nodes
n_ofVisited = []
currentNode = []

#Comparison Lists
list_A = ["A", "A", "A", "A"]
list_B = ["B", "B", "B", "B"]
list_C = ["C", "C", "C", "C"]
list_D = ["D", "D", "D", "D"]

#Successor functions
def succ():
  print("Test")

#Should take in 4 columns/lists
def uniform_cost_graph_search(col1, col2, col3, col4, col5, col6): 
  mainCol = [col1, col2, col3, col4, col5, col6]
  
  print("\n")

  #Check if the input is already arranged
  if (col1 == list_A and col2 == list_B and col3 == list_C):
    #Stack Creations with the checking conditions for ones with dot
    for i in range(len(col1) -1, -1, -1):
      print(col1[i] + " " + col2[i] + " " + col3[i] + " " + col4[i], end = ' ')
      try:
        print(col5[i], end = ' ');  
      except:
        print(".", end = ' ');

      try:
        print(col6[i], end = ' ');  
      except:
        print(".");
    print("\n(The input is already sorted)\n")

  #Algorithm Start
  #Always try with the first column
  #If not solveable when start with one then change next column to be the initial state
  #Move priority is same stack and next is empty stack = First few moves
  #After everything has been moving for awile, change priority to base on cheapest moves 
  #(Store the empty stacks element in one array to indicate that these elements will be the cheapest)
  #The problem right now is how to distinguish between nodes in different stacks
  increment = 0
  for i in range (6):
    print("Step " + increment)
    for j in range (6):
      if mainCol[i](len(mainCol[i])) == mainCol[j](len(mainCol[j])) or len(mainCol[j]) == 0:
        currentNode.append(mainCol[i](len(mainCol[i])))
        mainCol[i].remove(currentNode)
        currentNode.clear() #Clears all the nodes inside the currentNode, ready to use for next round
  increment = increment + 1 


  """
  for i in range (col1):
    for j in range (col1):
      if (col1[i][len(col1[i])] == col1[j][len(col1[j])] or len(col1[j]) == 0):
        #Add the moving element to the frontier
        #Adds only two elements into the frontier since there are only empty stacks to compare
        frontier.append() 
        col1.remove() #Remove the element from that column that we are working with
  """