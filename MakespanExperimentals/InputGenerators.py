import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import special

u = np.random.uniform(100,500,10000)
z = np.random.zipf(2.00,10000)
n = np.random.normal(300,100,10000)

normalizedInput = [0]*10000
for i,v in enumerate(n):
    normalizedInput[i] = v

uniformInput = [0]*10000
for i,v in enumerate(u):
    uniformInput[i] = v

zipfianInput = [0]*10000
for i,v in enumerate(result):
    zipfianInput[i] = v

print(zipfianInput)