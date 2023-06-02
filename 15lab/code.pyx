from math import sqrt, cos
import cython
@cython.boundscheck(False)
@cython.wraparound(False)
  
def main():
    n = 10
    m = 10

    f = lambda x: sqrt(x+2) - sqrt(x) - 3/11

    g = lambda x: ((3*(x**2) - 11) / ((-x**3) - 2))
    A = [[f(i) + g(j) for j in range(1, n + 1)] for i in range(1, m + 1)]
    sum = 0
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j]
            sum+=A[i][j]
    tot = 1/100 * sum
    print(round(tot,6))


if __name__ == "__main__":
    main()
