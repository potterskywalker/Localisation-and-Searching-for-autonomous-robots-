p=[0.2,0.2,0.2,0.2,0.2] #prior probability


world=['green','red','red','green','green']
Z = 'green' # measurement
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
