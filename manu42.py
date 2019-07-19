a1,b1=map(int,input().split())
count=0
for m in range(a1,b1+1):
    if m>1:
        for n in range(2,m):
            if(m%n==0):
                break
        else:
            count=count+1
print(count)

