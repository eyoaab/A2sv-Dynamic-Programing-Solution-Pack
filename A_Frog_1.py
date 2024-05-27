n = int(input())
nums = list(map(int,input().split()))
dp =  [float('inf') for i in range(n)]
dp[0] = 0
dp[1] = abs(nums[1] - nums[0])

for i in  range(2,n):
    height1 = abs(nums[i] - nums[i - 1]) + dp[i -1]
    height2 = abs(nums[i] - nums[i - 2])  + dp[i - 2]
    
    dp[i] = min(height1,height2)

print(dp[-1])    

    

