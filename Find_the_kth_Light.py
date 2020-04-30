#function to count the number 
# of numbers in range 1-num that 
# are divisible by given  
# prime numbers in switch[]
#n is length of switch[]
def findrank(num,n):
    inclusion=0
    exclusion=0
    global switch  #made switch(On state switches) global
    for i in range(1,1<<n):
        count=0
        product=1
        for j in range(n):
            if(i & (1<<j)):
                count+=1
                product=product*switch[j]
        if count%2==1:
            inclusion+=num//product
        else:
            exclusion+=num//product
    return inclusion-exclusion

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
    high=switch[0]*k
    #do binary search from k to min(switch)*k
    while(low<=high):
        mid=low+(high-low)//2
        # find the rank of mid. no of numbers that are divisible by any one prime in switch list
        if findrank(mid,n)>=k:
            res=mid
            high=mid-1
        else:
            low=mid+1
    print(res)
