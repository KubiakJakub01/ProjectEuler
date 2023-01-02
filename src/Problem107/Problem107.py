# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:18:50 2022

Problem 107: Minimal network
https://projecteuler.net/problem=107

@author: kuba
"""

'''
SOLUTION IDEA:
Krok 1:
    Zauważenie, że problem sprowadza się do wyznacznie maksymalnego drzewa rozpinającego (MST)
Krok 2:
    Zastosowanie algorytmu prima do wyznaczenia MST
Krok 3:
    Obliczenie sumy wag krawędzi grafu pierwotnego i odjęcie sumy uzystaknej po wyznaczeniu MST
Krok 4:
    Odjęcie od siebie obydwu wartosci
    
Output:
    Suma minimalna: 2153
    Suma całosc: 261832
    Wynik: 259679
--- 0.0009989738464355469 seconds ---

Stopień trudnosci: 35%
    
'''

import sys # Library for INT_MAX
import time

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.weight_sum = 0
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        #print ("Edge \tWeight")
        for i in range(1, self.V):
            #print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
            self.weight_sum += self.graph[i][parent[i]]
            
        print("Suma minimalna: {}".format(self.weight_sum))
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        self.printMST(parent)

temp_matrix = []
graph_matrix = []
with open("network.txt") as file:
    temp_matrix = file.readlines()
    
temp_matrix = [x.strip().replace('-', '0').split(',') for x in temp_matrix]

for matrix in temp_matrix:
    new_matrix = [int(x) for x in matrix]
    graph_matrix.append(new_matrix)

def solution():
    
    weight_sum = 0

    
    g = Graph(len(graph_matrix[0]))
    g.graph = graph_matrix
    g.primMST()
    
    for x in range(0, len(graph_matrix)):
        for y in range(0, len(graph_matrix)):
            if graph_matrix[x][y] != 0:
                weight_sum += graph_matrix[x][y]
                graph_matrix[y][x] = 0
    
    print("Suma całosc: {}".format(weight_sum))
    print("Wynik: {}".format(weight_sum-g.weight_sum))
    
start_time = time.time()
solution()
print("--- %s seconds ---" % (time.time() - start_time))












