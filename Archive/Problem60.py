# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:34:18 2018

@author: Admin

Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prim
"""
import math
from math import sqrt; 
from itertools import count, islice


class Klasa():
       
    def __init__(self):
        self.prime_list = self.inicialize_prime_numbers()
        self.suma = math.inf
        self.tab = [3]
        for prime in self.tab:
            #id_list = self.prime_list.index(prime)
            print('zakonczone dla {}'.format(prime))
            self.solution(lista=[prime], id_list=1)
            
    def isPrime(self, n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    
    def inicialize_prime_numbers(self):
        prime_list = [2]
        for i in range(3, 10000, 2):
            if self.isPrime(i):
                prime_list.append(i)
                
        return prime_list
    
    def solution(self, lista, id_list):        
        for next_prime in self.prime_list[id_list:]:
            print(lista)
            print('NP {}'.format(next_prime))
            for prime in lista:
                is_prime_1 = int(str(prime) + str(next_prime))
                is_prime_2 = int(str(next_prime) + str(prime))
                     
                if self.isPrime(is_prime_1) == False or self.isPrime(is_prime_2) == False:
                    #print('1: {} 2: {}'.format(is_prime_1, is_prime_2))
                    break      
            else:
                id_list = self.prime_list.index(next_prime)+1
                lista.append(next_prime)
                print(lista)
                if len(lista) == 5: 
                    print(lista)
                    if sum(lista) < self.suma:
                        #print('Nowa suma {} / Stara suma {}'.format(sum(lista), self.suma))
                        self.suma = sum(lista)
                        print(lista)
                        print("Suma: {}".format(self.suma))
                        return                
                self.solution(lista, id_list)
                    
klasa = Klasa()
        
        
    

