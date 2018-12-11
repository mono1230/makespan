

import math

C = 1.9201

def calcAvg(machineList, ind):
    avg = 0.0
    for i in range (ind-1,len(machineList)):
        avg += i 
    return avg

def isFlat(machineList,Kval,Ival):
    retVal = False
    steepConst = 2*(C-1)/(2*C - 3)
    if machineList[Kval-1] < steepConst*calcAvg(machineList,Ival+1):
        retVal = True
    return retVal

def MRAlg(m, inputList):
    #consts:
    I = int(math.ceil((5*C - 2*C*C - 1)*m/C)-1)
    K = 2*I - m 

    machineList = [0]*m
    for i in inputList:
        if isFlat(machineList,K,I) or machineList[I-1] + i > C*calcAvg(machineList,1):
            machineList[len(machineList)-1] += i 
        else:
            machineList[I-1] += i
        machineList.sort(reverse = True)
    return machineList[0]


print(MRAlg(5,inputA))
print(MRAlg(50,inputA))
print(MRAlg(150,inputA))
