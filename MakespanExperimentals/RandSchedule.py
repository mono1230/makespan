


import math
import random

#constant values for A1:
C1 = 1.832

#constant values for A2:
C2 = 2.0
C2PRIME = 1.885
ALPHA2 = 0.409/0.909


def calcMiuAvg(machineList,Kval):
    retVal = 0.0
    for i in range(Kval):
        retVal+=machineList[i]
    return retVal/Kval

def isBalanced(list,BETTA,K1):
    retVal = False

    if calcDelta(list,K1) <= BETTA*calcTotalLoad(list):
        retVal = True
    return retVal

def calcDelta(list,K1):
    delta = 0.0
    for i in range(K1,len(list)):
        delta += list[i]
    return delta

def calcTotalLoad(machineList):
    total = 0.0
    for i in machineList:
        total += i 
    return total

def isCritical(machineList,miu,ALPHA1,K1):
    retVal = False
    comparator = ALPHA1 * machineList[2*K1]
    if miu > comparator:
        retVal = True
    return retVal


def Algorithm1(machineList,input,K1,ALPHA1):
    for i in input:
        miu = calcMiuAvg(machineList,K1)
        if isCritical(machineList,miu,ALPHA1,K1) and (machineList[K1]+i) <= C1*calcTotalLoad(machineList)/len(machineList):
            machineList[K1] += i
        else:
            machineList[0] += i 
        machineList.sort()
    return machineList[len(machineList)-1]


def Algorithm2(machineList,input,K1,ALPHA1,K2,BETTA):
    compareList = [0]*len(machineList)
    listLength = len(machineList)
    for i in input:
        miu = calcMiuAvg(compareList,K1)
        if isCritical(compareList,miu,ALPHA1,K1) and (compareList[K1]+i) <= C1*calcTotalLoad(compareList)/len(compareList):
            compareList[K1] += i
        else:
            compareList[0] += i 
        compareList.sort()
        if isBalanced(compareList,BETTA,K1):
            gamma = max((C2PRIME*calcTotalLoad(machineList)/listLength),(C2*calcDelta(machineList,K1)/(listLength*BETTA)))
        else:
            gamma = C2*calcTotalLoad(machineList)/listLength

        if isCritical(machineList,miu,ALPHA1,K1) and (machineList[K2]+i) <= gamma:
            machineList[K2] += i 
        else:
            machineList[0] += i
        machineList.sort()
    return machineList[listLength-1]
    


def Rand(m,input):
    #consts:
    K1 = int(math.ceil(m*9.0/25))
    ALPHA1 = 1 - ( K1 - math.floor(0.074*m))/(2*0.916*K1)

    K2 = int(math.ceil(m*3.0/8))
    BETTA = 1 - (C1-1)*K1/m 


    machines = [0]*m
    makespan = 0
    if bool(random.getrandbits(1)):
        makespan = Algorithm1(machines,input,K1,ALPHA1)
    else:
        makespan = Algorithm2(machines,input,K1,ALPHA1,K2,BETTA)
    return makespan


print(Rand(5,inputA))
print(Rand(50,inputA))
print(Rand(150,inputA))
