#need more improvement
import numpy as np
import math
#dimensions, your_position, guard_position, distance



def solution(dimensions, your_position, guard_position, distance):
    pos = guard_position
    dim = dimensions
    myPos = your_position
    dist = distance
    npos = []
    npos.append(pos)
    npos.append([-1 * i for i in pos])
    npos.append([pos[0],-1*pos[1]])
    npos.append([-1*pos[0],pos[1]])
    temp = [2*dim[i] - pos[i] for i in range(len(dim))]
    npos.append(temp)

    npos.append([pos[0],temp[1]])
    npos.append([temp[0],pos[1]])
    npos.append([-1*pos[0],temp[1]])
    npos.append([temp[0],-1*pos[1]])
    
    a = []
    for i in range(len(npos)):
        t = [npos[i][0] - myPos[0],npos[i][1] - myPos[1]]
        if t[0] != 0 or t[0] != 0:
            a.append(t)
    i = 1
    while i < len(a):
        if a[i][0]*a[i][1] == 0:
            del a[i]
        i += 1
    print("Mid:-",a)
    i = 0
    count = 0
    while i < len(a):
        m = math.sqrt(a[i][0] **2 + a[i][1] ** 2)
        if m <= dist:
            count += 1
        else:
            break
        i +=1
    print("End:-",a)
    return count
