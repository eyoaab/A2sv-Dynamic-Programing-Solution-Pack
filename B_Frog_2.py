
from sys import stdin
input = lambda : stdin.readline().strip()

def solve():
    n, k = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    dp = [float("inf")] * n
    dp[-1] = 0
    for i in range(n-1, -1, -1):
        for j in range(1, k + 1):
            if i-j > -1:
                dp[i-j] = min(dp[i-j], dp[i]+abs(heights[i]-heights[i-j]))
    
    print(dp[0])

solve()