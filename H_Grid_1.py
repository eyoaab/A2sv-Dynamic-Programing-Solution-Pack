
from math import *
from heapq import *
from bisect import *
from collections import *
from sys import * 

linp = lambda: list(map(int, input().split()))
iinp = lambda: int(input())
inp = lambda: input()
MOD = 10 ** 9 + 7



def solve():
    r,c = linp()
    dp = [[1] + [0 for i in range(c-1)]]

    for _ in range(r):
        row = [0 for i in range(c)]

        row_  = inp()
        for i in range(c):
            if i != 0:
                if row_[i] == '.':
                    row[i] += dp[-1][i] + row[i - 1]
            else:
                if row_[i] == '.':
                    row[i] += dp[-1][i]       

        dp.append(row)

    print((dp[-1][-1]) % MOD)            



    


t = 1
for _ in range(t):solve()