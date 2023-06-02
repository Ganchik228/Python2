from math import *
def f(i):
    return sqrt(i+2) - sqrt(i) - 3/11

def g(j):
    return ((3*(j**2) - 11) / ((-j**3) - 2))
n = 10  
a = [[0]*n for _ in range(n)]
total_sum = 0
for i in range(n):
    for j in range(n):
        a[i][j] = f(i+1) + g(j+1) 
        total_sum += a[i][j]

tot = 1/100 * total_sum
print(round(tot, 6))

# print(f(10))
# print(g(10))
# import time
# start_time = time.time()
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")

