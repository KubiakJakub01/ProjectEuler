"""
Created on 05-01-2023 17:01

Problem 127: abc-hits
https://projecteuler.net/problem=127

author: KubiakJakub01
"""
# import libraries
import math
import time

LIMIT = 120000

# main solution function
def solution():
	LIMIT = 120000

	rads = [0] + [1] * (LIMIT - 1)
	for i in range(2, len(rads)):
		if rads[i] == 1:
			for j in range(i, len(rads), i):
				rads[j] *= i
	
	sortedrads = sorted((rad, n) for (n, rad) in enumerate(rads))
	sortedrads = sortedrads[1 : ]
	
	ans = 0
	for c in range(2, LIMIT):
		for (rad, a) in sortedrads:
			rad *= rads[c]
			if rad >= c:
				break
			b = c - a
			if a < b and rad * rads[b] < c and math.gcd(a, b) == 1:
				ans += c
	return str(ans)


if __name__ == "__main__":
    start_time = time.time()
    print(solution())
    print("--- %s seconds ---" % (time.time() - start_time))
