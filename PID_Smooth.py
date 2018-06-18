# -----------
# Smooth PID Control

from copy import deepcopy

# thank you EnTerr for this print function
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# define alpha = 0.5, belta = 0.1
def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
            
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(1,len(path)-1):
            for j in range(len(path[0])):
                temp = newpath[i][j]
                # implement two equations
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - (2*newpath[i][j]))
                
                change += abs(temp - newpath[i][j])               
    return newpath 

printpaths(path,smooth(path))
