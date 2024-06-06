n,m  = list(map(int,input().split()))
graph = [[]for i in range(n + 1)]
indeegre = [0 for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indeegre[b] += 1

# memo = {}
dp = [0 for i in range(n +1)]

for i in range(n + 1):
    for node in graph[i]:
        dp[node] = max(dp[i] + 1,dp[node])
print(max(dp))    
print(dp)



# def dfs(index):
#     if index in memo:
#         return memo[index]
#     if len(graph[index]) == 0:
#         return 0
#     max_ = 0
#     for i in graph[index]:
#         max_ = max(max_,1 + dfs(i))

#     memo[index]  = max_
#     return memo[index]   

# ans =  0
# for i in range(1,n+1):
#     if indeegre[i] == 0:
#         ans = max(ans,dfs(i))

# # print(memo)
# print(ans)         
