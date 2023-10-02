def reverse_nums(a):
    nums=a
    width=1 # since we break the loop when nums<10, so at least it will hace a 10^1 value  
    if -10<a and a<10:
         return a
    while True:
        nums=nums//10
        print(nums)
        width+=1
        if nums<10 and nums >0:
            break
    print(width)
    nums=a
    mul=10
    tmp=0
    result=0
    while  True:
        tmp=nums%mul
        # print(tmp)
        result=result+tmp*(mul**(width-1))
        # print(width*mul*tmp)
        nums=nums//10
        width-=1
        if nums==0:
            break
    return result

print(reverse_nums(1234567891))  
             
        
        
            