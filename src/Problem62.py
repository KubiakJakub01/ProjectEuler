# -*- coding: utf-8 -*-
"""
Problem 62 (Cubic permutations)
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits
which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def solution():
    #tab = [2]
    cube_list = []
    flag = True
    number = 1
    while flag:
        cube = pow(number, 3)
        number+=1
        #print('Cube: {}'.format(cube))
        if cube_list:
            #print('Wielkosc cube_list: {}'.format(len(cube_list)))
            for i in range(0, len(cube_list)):
                if sorted(str(cube)) == sorted(str(cube_list[i][0])):
                    cube_list[i][1]+=1
                    print("Cos sie ruszylo {}".format(cube_list[i][1]))
                    if cube_list[i][1] == 5:
                        print("Wynik: {}".format(cube_list[i][0]))
                        flag = False
                        return 0
                    break
            else:
                tab = [cube, 1]
                #print('Cube: {}'.format(cube))
                cube_list.append(tab)
        else:
            #print("1 iteracja")
            tab = [cube, 1]
            cube_list.append(tab)
        
solution()
        