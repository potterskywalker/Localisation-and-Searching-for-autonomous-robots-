# Search Algorithm

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # open list elements are of the type: [g,x,y]
    
    closed=[[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    
    x = init[0]
    y = init[0]
    g = 0
    
    open = [[g,x,y]]
    
    found = 0 # flag that is set when search complete
    resign = 0 # flag set if we can't find expand
    
#    for debugging
#    print 'initial open list: '
#    for i in range(len(open)):
#        print open[i]
#    print '----'
    
    while found is 0 and resign is 0:
        if len(open) == 0:
            resign = 1
            print 'fail'
        
        else:
            open.sort()
            open.reverse()
            next = open.pop() # remove the smallest element in open list
            # print 'take list item'
            # print next
            x = next[1]
            y = next[2]
            g = next[0]
            
            #check if we are at the goal
            
            if  x == goal[0] and y == goal[1]:
                found = 1
                print next
            
            else:
                
                #expand surviving element and add to new open list
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    # if x2, y2 fall into the grid
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2< len(grid):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0: # if x2, y2 is not closed and is valid
                            
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            
                            #print 'append list item'
                            #print [g2, x2,y2]
                            closed[x2][y2]=1

                


print search(grid,init,goal,cost)