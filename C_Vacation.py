n  = int(input())
a,b,c = list(map(int,input().split()))
if n == 1:
    print(max(a,b,c))
else:
    for i in range(n - 1):
        row = list(map(int,input().split()))
        row[0] += max(b,c)  
        row[1] += max(a,c)  
        row[2] += max(a,b)  
        a,b,c = row   
    print(max(a,b,c))
