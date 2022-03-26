import numpy as np

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
def DFS_getPath(start, end, visited):

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
        path = DFS_getPath(start, end, visited)

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
    
    path=[]
    visited={}
   
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
    return visited, path

