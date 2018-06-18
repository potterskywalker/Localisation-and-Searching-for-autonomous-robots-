p=[0,1,0,0,0]


world=['green','red','red','green','green']
Z = ['red']
pHit = 0.6
pMiss = 0.2

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

print sense(p,Z)

#consider movement, U is the number of cells that the robot is moving to the right
def move(p, U):
    q=[]
    for i in range(len(p)):
        q.append(p[(i-U)%len(p)])
    return q



print move(p,1)
