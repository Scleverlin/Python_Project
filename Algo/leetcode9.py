def calculate_width_and_num(a):
    width=0
    tmp=0
    num=[]
    while True:
        tmp=a%10
        num.append(tmp)
        a=a//10
        width=width+1
        if a==0:
            break
    return width,num

a=200
print(calculate_width_and_num(a))

def reversible_num(a):
    if a<0:
        return False
    width,num=calculate_width_and_num(a)
    for i in range(width//2):
            if num[i]!=num[width-1-i]:
                return False
    return True

a=-121
print(reversible_num(a))

