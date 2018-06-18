# DP- Stochastic


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    

    # dynamic programming
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True
                        #calculate the three ways to propagate value
                        
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                            
                        v2 = cost_step
                        for i in range(-1, 2):
                            a2 = (a + i) % len(delta)
                            x2 = x + delta[a2][0]
                            y2 = y + delta[a2][1] 
                            
                            if i == 0:
                                p2 = success_prob
                            else:
                                p2 = (1.0 - success_prob) /2.0
                                    
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                
                                v2 += p2 * value[x2][y2]
                            else:
                                v2 += p2 * collision_cost
        
                        if v2 < value[x][y]:
                            change = 1
                            value[x][y] = v2
                            policy[x][y] = delta_name[a]
        
    
    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 1000
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print row
for row in policy:
    print row

