p=[0,1,0,0,0]


world=['green','red','red','green','green']
Z = ['red','green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2

#inaccurate movement due to robot motion
pExact=0.8
pOvershoot=0.1
pUndershoot=0.1

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
        s = pExact*p[(i-U)%len(p)]
        s = s+pOvershoot*p[(i-U-1)%len(p)]
        s = s+pUndershoot*p[(i-U+1)%len(p)]
        q.append(s)
        
    return q

for k in range(1000):
    p=move(p,1)

print p
