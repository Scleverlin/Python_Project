def find_mid_num(a,b):
    m=len(a)
    n=len(b)
    if m>n:
        a,b,m,n=b,a,n,m# n is the longer one
    i=(m+1)//2
    j=0
    while True:
        j=(m+n+1)//2-i
        if a[i-1]<=b[j] and b[j-1]<=a[i]:
            break
        elif a[i-1]>b[j]:
            i=(i+1)//2
        elif b[j-1]>a[i]:
            i=i+(m-i+1)//2
    
    min_mid=max(a[i-1],b[j-1])
    max_mid=min(a[i],b[j])
    return (min_mid+max_mid)/2 if (m+n)%2==0 else min_mid
    
        
a=[1,2,3,4]
b=[1,2,3,4,5,7,8,9,10]

print(find_mid_num(a,b))        
