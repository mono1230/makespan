
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

print(ListSchedule(5,inputA))
print(ListSchedule(50,inputA))
print(ListSchedule(150,inputA))
