'''
Problem 78: Coin partitions
https://projecteuler.net/problem=78
'''

'''
In how many ways numer can be written???
'''
%matplotlib qt

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math


#Alg for count ways from https://www.geeksforgeeks.org/ways-to-write-n-as-sum-of-two-or-more-positive-integers/
def CountWays(n):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n ):
        for j in range(i , n + 1):
            table[j] +=  table[j - i]
    return table[n]


def f(n):
    wynik = round((1/(4*n*math.sqrt(3)))*np.exp(math.pi*math.sqrt((2*n)/3)))
    return wynik

def solution():
    N = 1000000
    #n=10
    result = 1
    dict_n = {}
    #while result % N != 0:
        #n+=1
    for n in range(1509,2510,10):
        result = (CountWays(n)+1)
        #dict_n[n] = result
        #result_2 = f(n)
        #print('alg: {} formula: {}'.format(result, result_2))
        if result % 1000 == 0:
            print('n: {} p(n): {}'.format(n, result))
    
    '''x, y = dict_n.keys(), list(dict_n.values())
    ml = MultipleLocator(N)
    plt.plot(x, y)
    plt.title('p(n)')
    plt.xlabel('n')
    #plt.yticks(np.arange(y[0], y[-1], step=100), minor=True)
    plt.axes().yaxis.set_minor_locator(ml)
    plt.grid()
    plt.show()'''

    #print(n)


solution()
