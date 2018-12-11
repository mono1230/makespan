

def sortedApproximation(numOfMachines, input):
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

print(sortedApproximation(5,inputA))
print(sortedApproximation(50,inputA))
print(sortedApproximation(150,inputA))