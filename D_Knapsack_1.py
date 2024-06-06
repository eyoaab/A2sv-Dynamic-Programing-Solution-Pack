
from sys import stdin

input = lambda : stdin.readline().strip()

def lint():
    return list(map(int, input().split()))

def intp():
    return int(input())
    
def strp():
    return input()

def lstr():
    return list(input().split())

def solve():
    N, W = lint()
    grid = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for j in range(1, N+1):
        w, v = lint()
        for i in range(1, W+1):
            if i-w >= 0:
                grid[j][i] = max(grid[j-1][i], grid[j-1][i-w]+v)
            else:
                grid[j][i] = grid[j-1][i]
    
    print(grid[-1][-1])
        

solve()