


world=['green','red','red','green','green']
p=[0.2,0.2,0.2,0.2,0.2]   # prior belief
Z = ['red','green'] #Z is the measurements, firstly detect red, secondly detect green
motions = [1,1]     #move right and right again
pHit = 0.6
pMiss = 0.2

#inaccurate movement due to robot motion
pExact=0.8
pOvershoot=0.1
pUndershoot=0.1

# sense function computes the posterior probability
def sense(p,Z):
    q=[]
    
    for i in range(len(p)):
        hit = (Z ==world[i] )
        q.append(p[i]*(hit*pHit+(1-hit)*pMiss)) #if hit=0,p[i]*pMiss, otherwise p[i]*pHit

    #normalise the probability
    s = sum(q)
    for i in range (len(p)):
        q[i] = q[i]/s
    
    return q


#consider movement, U is the number of cells that the robot is moving to the right
def move(p, U):
    q=[]
    for i in range(len(p)):
        s = pExact*p[(i-U)%len(p)]              #move p[i] to the right by U cell
        s = s+pOvershoot*p[(i-U-1)%len(p)]
        s = s+pUndershoot*p[(i-U+1)%len(p)]
        q.append(s)
        
    return q

for k in range(len(Z)):  #robot sees red and move 1 cell and sees red again and move 1 more cell.
    p = sense(p,Z[k])
    p = move(p,motions[k])
print p
