'''
Problem 85: Counting rectangles
https://projecteuler.net/problem=85
'''

'''
Formula: m(m+1)n(n+1)/4
Where grid: MxN
Some examples:
52x52 == 1898884
53x53 == 2047761
'''

def f(m,n):
    return int(m*(m+1)*n*(n+1)/4)

def solution():
    N = 2000000
    min_diff = 100
    area = 0
    for i in range(1,52):
        grid = 52
        prev_rectangles = 0
        rectangle = 0
        while N > rectangle:
            prev_rectangles = rectangle
            rectangle = f(grid,i)
            grid += 1
        grid -= 1
        diff = abs(N-rectangle)
        if diff < min_diff:
            min_diff = diff
            area = grid*i
        grid -= 1
        diff = abs(N-prev_rectangles)
        if diff < min_diff:
            min_diff = diff
            area = grid*i
    print('area: {}'.format(area))

solution()
