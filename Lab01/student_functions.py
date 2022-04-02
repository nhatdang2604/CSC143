import numpy as np
import math
from queue import PriorityQueue

def DFS_getVisited(matrix, currentNode, end, visited):
    
    #terminate condition for recursive
    if (currentNode == end):
        return visited
    
    #recursive part
    for node, weight in enumerate(matrix[currentNode]):

        if 0 < weight:                                                  #if there is any path from currentNode -> node
            if node not in visited.keys():                              #if the node has not been visited yet
                visited[node] = currentNode                             #mark that the node is visited
                visited = DFS_getVisited(matrix, node, end, visited)    #the current node now is the node

    #return the current visisted, if there are:
    #   0) The current node has no adjacency node
    #   1) All the adjacency node of current node is visited
    return visited

#Trace the path from start to end, 
# by using the builded visited
def tracePathFromVisited(start, end, visited):

    #the answer path
    path = []

    #Iterate from end -> start
    nodeIterator = end

    #Trace from end -> start (because visited[start] = None)
    while nodeIterator != None:
        path.append(nodeIterator)
        nodeIterator = visited[nodeIterator]

    #Reverse the path to become start -> end
    path.reverse()

    #Return the reversed path
    return path
    
def DFS(matrix, start, end):
    """
    FS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
    path=[]
    visited={}

    #init the start node's visitor
    visited[start] = None

    #Build the visited dictionary
    visited = DFS_getVisited(matrix, start, end, visited)
    
    #Only trace the path, if there is any path from start -> end
    if end in visited.keys():
        path = tracePathFromVisited(start, end, visited)

    return visited, path

def BFS(matrix, start, end):
    """
    BFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    #Given variable
    path=[]
    visited={}
   
    #the queue for storing the node's adjacency
    #   for iterating
    queue = []

    #initialize the pre-node to reach to start node
    visited[start] = None

    #store the start node into the queue
    queue.append(start)

    #flag to check, if the end node is popped from the queue
    isEnd = False

    if start != end:
        while not isEnd:

            #the iterator for scanning each matrix
            currentNode = queue.pop(0)

            #Start to iterate
            for node, weight in enumerate(matrix[currentNode]):
                if weight > 0:
                    if node not in visited.keys():
                        visited[node] = currentNode
                        if node == end:
                            isEnd = true
                            break
                        queue.append(node)
    #clear the queue after using
    queue.clear()
                
    #Only trace the path, if there is any path from start -> end
    if end in visited.keys():
        path = tracePathFromVisited(start, end, visited)

    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}

    #visisted, but with cost
    visitedAndCost = {}

    #The priority queue to get the minimum distance node 
    #  which is adjancency to the current node
    priorityQueue = PriorityQueue()

    #mark the start node is visited
    visitedAndCost[start] = (0, None)

    #put the start node into priority queue
    priorityQueue.put((0, start))   #0 is the init distance

    while not priorityQueue.empty():

        #get the minimum node which in the pqueue
        currentNode = priorityQueue.get()
        
        #get the variable for code readability
        minWeight = currentNode[0]
        minNode = currentNode[1]

        #terminate condition
        if minNode == end:
            break

        #iterate over all the adjancency node of the minNode
        for node, weight in enumerate(matrix[minNode]):

            #if there is a path from minNode -> node
            if weight>0:

                #calculate the total cost
                totalCost = minWeight + weight

                #if the node has not been visited yet
                if node not in visitedAndCost.keys():

                    #mark as the node was visited
                    visitedAndCost[node] = (totalCost, minNode)

                    #put the node into priority queue, with weight = sum weight
                    priorityQueue.put((totalCost, node))

                else:
                    
                    #check if the current path from somewhere -> node is longer than
                    #   from minNode -> node:
                    #       If yes: update the new path to minNode -> node
                    #       else, do nothing
                    if visitedAndCost[node][0] > totalCost:
                        visitedAndCost[node] = (totalCost, minNode)
                        priorityQueue.put((totalCost, node))

    #update the visited from visitedAndCost
    for key in visitedAndCost.keys():
        visited[key] = visitedAndCost[key][1]

    #find the path base on the visited
    if end in visited.keys():
        path = tracePathFromVisited(start, end, visited)
        
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}

    #The priority queue to get the minimum distance node 
    #  which is adjancency to the current node
    priorityQueue = PriorityQueue()

    #mark the start node is visited
    visited[start] = None

    #put the start node into priority queue
    priorityQueue.put((0, start))   #0 is the init distance

    #flag to check if the end path is found
    isEndFound = False

    #loop until found the end node
    while not isEndFound:

        #get the minimum node which in the pqueue
        currentNode = priorityQueue.get()
        
        #get the variable for code readability
        minWeight = currentNode[0]
        minNode = currentNode[1]

        #iterate over all the adjancency node of the minNode
        for node, weight in enumerate(matrix[minNode]):

            #if there is a path from minNode -> node
            if weight>0:

                #if the node has not been visited yet
                if node not in visited.keys():

                    #mark as the node was visited
                    visited[node] = minNode

                    #check if the node is the end node => finish the loop
                    if end == node:
                        isEndFound = True
                        break
                    
                    #put the node into priority queue, with weight = sum weight
                    priorityQueue.put((minWeight + weight, node))

    #find the path base on the visited
    if end in visited.keys():
        path = tracePathFromVisited(start, end, visited)

    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}

    #visisted, but with cost
    #cost = f(x) = g(x) + h(x)
    visitedAndCost = {}

    #The priority queue to get the minimum cost node
    #  which is adjancency to the current node
    priorityQueue = PriorityQueue()

    #mark the start node is visited
    visitedAndCost[start] = (0, None)

    #put the start node into priority queue
    priorityQueue.put((0, start))   #0 is the init distance

    #get the end node'coordinate
    endCoordinate = pos[end]

    while not priorityQueue.empty():

        #get the minimum node which in the pqueue
        currentNode = priorityQueue.get()
        
        #get the variable for code readability
        minWeight = currentNode[0]
        minNode = currentNode[1]

        #terminate condition
        if minNode == end:
            break

        #iterate over all the adjancency node of the minNode
        for node, weight in enumerate(matrix[minNode]):

            #if there is a path from minNode -> node
            if weight>0:

                #get the cooridnate of the adjancency node
                nodeCoordinate = pos[node]

                #calculate the value f(x) base on total weigth + heuristic
                dx = (endCoordinate[0] - nodeCoordinate[0])
                dy = (endCoordinate[1] - nodeCoordinate[1])
                h_x = math.sqrt(dx * dx + dy * dy)  #heuristic base on the euclidean distance
                g_x = minWeight + weight            #total weight  
                
                #calculate the total cost (the f(x))
                totalCost = h_x + g_x

                #if the node has not been visited yet
                if node not in visitedAndCost.keys():

                    #mark as the node was visited
                    visitedAndCost[node] = (totalCost, minNode)

                    #put the node into priority queue, with weight = sum weight
                    priorityQueue.put((totalCost, node))

                else:
                    
                    #check if the current path from somewhere -> node is longer than
                    #   from minNode -> node:
                    #       If yes: update the new path to minNode -> node
                    #       else, do nothing
                    if totalCost < visitedAndCost[node][0]:
                        visitedAndCost[node] = (totalCost, minNode)
                        priorityQueue.put((totalCost, node))

    #update the visited from visitedAndCost
    for key in visitedAndCost.keys():
        visited[key] = visitedAndCost[key][1]

    #find the path base on the visited
    if end in visited.keys():
        path = tracePathFromVisited(start, end, visited)


    return visited, path

