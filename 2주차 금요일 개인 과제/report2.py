N = int(input()) 
 
Num = 0 
for i in range(N): 
    answer = d = i 
    while d > 0: 
        answer += (d % 10) 
        d //= 10 
 
    if answer == N: 
        Num = i 
        break 

print(Num) 
