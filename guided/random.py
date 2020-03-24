from util import Stack, Queue  # These may come in handy
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4
# 1. translate the problem into terminology we know
# 2. build the graph
# 3. traverse the graph
def island_counter(matrix):
    # create a visited matrix
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    # for all nodes:
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
        # if node is not visited:
            if not visited [row][col]:
            #If we hit a 1 that has not been visited
                if matrix[row][col] == 1:
                #mark visited
                #traverse all connected nodes, marking as visited
                    visited = dft(row, col, matrix, visited)
                    #increment island count
                    island_count += 1
        return island_count

def dft(start_row, start_col, matrix, visited):
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(start_row, start_col)
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            row = v[0]
            col = v[1]
            # Check if it's been visited
            # If it hasn't been visited...
            if not visited[row][col]:
                # Mark it as visited
                visited[row][col]
                visited.add(v)
                # Push all it's neighbors onto the stack
                for neighbor in get_neighbors(row ,col,matrix):
                    s.push(neighbor)
        return visited

def get_neighbors(row, col, matrix):
    '''
    returns a list f neighboring 1 tuples in the form [(row, col)]
    '''
    neighbors = []
    # check north
    if row > 0 and matrix[row-1][col]:
        neighbors.append( ( row-1, col))
    # check south
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append( (row+1, col))
    # check East
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append( (row, col+1))
    # check west
    if col < 0 and matrix[row][col-1] == 1:
        neighbors.append( (row, col-1))
    return neighbors