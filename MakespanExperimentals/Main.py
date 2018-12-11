import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import special
import math
import random



#Largest Processing Time IMPLEMENTATION=====================================
def SortedApproximation(numOfMachines, input):
    machines = [0]*numOfMachines
    input.sort(reverse = True)
    for i in input:
        (p,q) = min((a,b) for b,a in enumerate(machines))
        machines[q] = machines[q]+i

    makespan = 0
    for j in machines:
        if j > makespan:
            makespan = j
    return makespan

#ListSchedule IMPLEMENTATION=====================================
def ListSchedule(numOfMachines, input):
    machines = [0]*numOfMachines
    for i in input:
        (p,q) = min((a,b) for b,a in enumerate(machines))
        machines[q] = machines[q]+i

    makespan = 0
    for j in machines:
        if j > makespan:
            makespan = j
    return makespan

#RAND IMPLEMENTATION=====================================

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


#MR Implementation===========================
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




def main():

    uni1000 = np.random.uniform(100,500,1000)
    uni10000 = np.random.uniform(100,500,10000)
    zipf1000 = np.random.zipf(1.98,1000)
    zipf10000 = np.random.zipf(1.98,10000)
    norm1000 = np.random.normal(300,100,1000)
    norm10000 = np.random.normal(300,100,10000)

    normArr1000 = [0]*1000
    for i,v in enumerate(norm1000):
        normArr1000[i] = v
    normArr10000 = [0]*10000
    for i,v in enumerate(norm10000):
        normArr10000[i] = v

    uniArr1000 = [0]*1000
    for i,v in enumerate(uni1000):
        uniArr1000[i] = v
    uniArr10000 = [0]*10000
    for i,v in enumerate(uni10000):
        uniArr10000[i] = v

    zipfArr1000 = [0]*1000
    for i,v in enumerate(zipf1000):
        zipfArr1000[i] = v
    zipfArr10000 = [0]*10000
    for i,v in enumerate(zipf10000):
        zipfArr10000[i] = v

    machineNum = [5,50,150]

    file = open("result.txt","w")
    file.write('Input Uniform Distribution 1000:\n')

    for i in range(3):
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], uniArr1000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], uniArr1000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], uniArr1000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], uniArr1000)) + "\n")

    file.write('\n')
    
    file.write('Input Uniform Distribution 10000:\n')

    for i in range(3):
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], uniArr10000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], uniArr10000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], uniArr10000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], uniArr10000)) + "\n")
    file.write('\n')

    file.write('Input Normal Distribution 1000:\n')

    for i in range(3):
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], normArr1000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], normArr1000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], normArr1000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], normArr1000)) + "\n")
    file.write('\n')
    
    file.write('Input Normal Distribution 10000:\n')

    for i in range(3):
        
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], normArr10000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], normArr10000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], normArr10000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], normArr10000)) + "\n")
    file.write('\n')

    file.write('Input Zipf Distribution 1000:\n')

    for i in range(3):
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], zipfArr1000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], zipfArr1000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], zipfArr1000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], zipfArr1000)) + "\n")
    file.write('\n')

    file.write('Input Zipf Distribution 10000:\n')

    for i in range(3):
        file.write('m = '+str(machineNum[i])+" machines\n")
        file.write('Approximate Opt: ')
        file.write(str(SortedApproximation(machineNum[i], zipfArr10000)) + "\n")
        file.write('List Schedule: ')
        file.write(str(ListSchedule(machineNum[i], zipfArr10000)) + "\n")
        file.write('MR Algorithm: ')
        file.write(str(MRAlg(machineNum[i], zipfArr10000)) + "\n")
        file.write('Rand Algorithm: ')
        file.write(str(Rand(machineNum[i], zipfArr10000)) + "\n")
    file.write('\n')



if __name__ == "__main__":
    main()

