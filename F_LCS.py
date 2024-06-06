s = input()
t = input()

n =  len(s)
m = len(t)
memo = {}
answer = ""

def dp(index1,index2):
    if index1 >= n or index2 >= m:
        return ""

    if(index1,index2) in memo:
        return memo[(index1,index2)]

    if s[index1] == t[index2]:
        memo[(index1,index2)] =  s[index1] + dp(index1 + 1, index2 + 1)
    else:

        first = dp(index1 + 1,index2)
        second = dp(index1 ,index2 + 1)
        if len(first) >= len(second):
            memo[(index1,index2)] =  first
        else:
            memo[(index1,index2)] =  second


    return memo[(index1,index2)]
print(dp(0,0))
 
  



    
      
