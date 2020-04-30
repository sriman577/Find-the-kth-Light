def findrank(num,n):
    rank=0
    global switch
    for i in range(1,1<<n):
        count=0
        product=1
        for j in range(n):
            if(i & 1<<j):
                count+=1
                product=product*switch[j]
        if count%2==1:
            rank+=num//product
        else:
            rank-=num//product
    return rank

t=int(input())
for itr in range(t):
    s=input()
    k=int(input())
    switch=[]
    for i in range(40):
        if s[i]=='1':
            switch.append(i+1)
    low=k
    res=-1
    n=len(switch)
    high=k*switch[0]
    while(low<=high):
        mid=low+(high-low)//2
        if findrank(mid,n)>=k:
            res=mid
            high=mid-1
        else:
            low=mid+1
    print(res)
