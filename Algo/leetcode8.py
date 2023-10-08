def convert_string_to_num(a):
    result=0
    flag=0
    mul=1
    for char in a:
        if char==' ' and flag==0:
            continue
        elif flag==1 and (char<'0' or char>'9') :
            break
        elif flag==0 and char ==' ':
            continue
        if char =='-':
            mul=-1
            continue
        flag=1
        result=result*10+int(char)
        
    result=result*mul
    return result

a='     -123 a '
print(convert_string_to_num(a))
            
                        