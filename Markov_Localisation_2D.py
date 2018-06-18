#Given wolrd is a two dimensional m x n matrix with only 2 colours
#Motion:[0,0]-no move, [0,1]-right, [0,-1]-left, [1,0]-down, [-1,0]-up; cyclic


colours = [['red', 'red', 'red'],
          ['red', 'green', 'red'],
          ['red', 'red', 'red']]
#Z is the measurements
Z = ['green']                                      
motions = [[0,-1]]
sensor_right = 0.8
move_right = 0.8



#inaccurate movement and inaccurate sensor
sensor_wrong = 1.0 - sensor_right
p_stay = 1.0 - move_right


# sense function computes the posterior probability
def sense(p, colours, Z):
    #construct a zero matrix
    q=[[0.0 for row in range(len(p[0]))] for clo in range(len(p))]
    
    
    #if hit=0,p[i]*pMiss, otherwise p[i]*pHit
    s = 0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (Z == colours[i][j])
            q[i][j] = p[i][j]*(hit*sensor_right+(1-hit)*sensor_wrong) 
            s += q[i][j]
            
    #normalise the probability
    for i in range (len(p)):
        for j in range (len(p[i])):
            q[i][j] = q[i][j]/s
    
    return q


#Motion:[0,0]-no move, [0,1]-right, [0,-1]-left, [1,0]-down, [-1,0]-up; cyclic
def move(p, motion):
    #construct a zero matrix
    q=[[0.0 for row in range(len(p[0]))] for clo in range(len(p))]
    
    for i in range(len(p)):
        for j in range(len(p[i])):
            
            #in this case inaccurate motion = does not move
            q[i][j] = move_right * p[(i-motion[0] % len(p))][(j-motion[1]) % len(p[i])] + (p_stay*p[i][j])           
           
    return q


def show(p):
    for i in range (len(p)):
        print p[i]


#main function
if len(Z) != len(motions):
    raise ValueError, "error in size of measurement/motion"


#initialise the prior belif in nxm matrix (prior belif is an uniform distribution in this case)
initial_belif = 1.0/ float(len(colours))/ float(len(colours[0]))
p = [[initial_belif for row in range(len(colours[0]))] for col in range(len(colours))]


for k in range(len(Z)):

    #robot sense one cell and move one cell
    p = move(p,motions[k])
    p = sense(p,colours,Z[k])

show(p)
