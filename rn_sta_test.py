import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import stats
from scipy.stats import chi2


N = 10000       #number of random numbers
r = [0.0] * N   #random numbers array
X = [0.0] * N   #delay-k statistiacal test　array
Y = [0.0] * N   #equiprobability statistiacal test array

def main():
    i = 0
    print("Generate random numbers")
    for i in range(0,N,1):
        r[i] = random.random()
    
    deley_k_test(N, r)
    hist(N, r)
    print("test end")

def deley_k_test(N, r):
    print("######### delay-k statistiacal test #########\n")
    i = 0
    j = 0
    k = 1 #delay-k test parameter
    sum_cov = 0.0
    count = 0
    for i in range(0,N,1):
        if((i + k) > (N - 1)):
            j = i - N + k
            X[i] = r[i]
            Y[i] = r[j]
            sum_cov += X[i] * Y[i]
        else:
            X[i] = r[i]
            Y[i] = r[i + k]
            sum_cov += X[i] * Y[i]
    z = (12.0 / N * sum_cov - 3) * math.sqrt(N) / math.sqrt(13)
    
    if(-1.96 < z < 1.96):
        count += 1
    print("delal-k statistical value:", z)
    if(count == 0):
        print("count:",count, "irregralty OK",)
    else:
        print("count:",count, "No irregralty cheak the random nunmber sequnece\n")

def hist(N, r):
    print("######### quiprobability statistiacal test #########\n")
    i = 0
    int_r = 0
    numbin = 10
    bin_weight = 10
    S = 0.0
    A = 0.0
    print("num bin:", numbin)
    
    hist = [0] * (int(numbin) + 1)
    S_array = np.zeros(((numbin),2))

    for i in range(0, N, 1):
        int_r = int(r[i] * bin_weight)
        hist[int_r] += 1

    print("histgram")
    for i in range(0, (numbin+1), 1):
        print(i,hist[i])
   
    ex_value = int(N/(numbin))
    print("kitaichi",ex_value)

    for i in range(0, (numbin), 1):
       S_array[i][1] = (math.pow(hist[i] - ex_value, 2) / ex_value)

    print("S_array")
    for i in range(0, (numbin), 1):
        print(i, S_array[i][1])
    
    S = np.sum(S_array)
    print("S", S)

    p = 0.05
    A = sp.stats.chi2.isf(p,(numbin-1))
    print("A:", A)

    if(S < A):
        print("quiprobability OK\n")
    else:
         print("No quiprobability cheak the random nunmber sequnece\n")

if __name__ == '__main__':
    main()