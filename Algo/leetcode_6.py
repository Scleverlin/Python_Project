def z_string_convert(a,nums):
    space_sym=" "

    result_list=[]
    tmp_list=[]
    for i in range (nums):
        space_need=space_sym*(nums-2)
        mul=1
        tmp_list=a[i]
        add=2*nums-2
        # ingnore nums within space first
        while True:
            tmp_list+=space_need
            if i+mul*add>len(a)-1:
                break
            tmp_list+=a[i+mul*add]
            mul+=1
        result_list.append(tmp_list)
    #replace space 
    print(result_list)
    n_add=0
    for order,list in enumerate(result_list):
        mul=1
        add=2*nums-2
        posistion=nums-order-1
        # print(list)
        if order==0:
            continue
        if order==len(result_list)-1:
            break
        print(a[nums+n_add])
        while True:
            if nums+n_add+(mul-1)*add >len(a)-1:
                break
            result_list[order]=result_list[order][:posistion]+a[nums+n_add+(mul-1)*add]+result_list[order][posistion+1:]
            posistion=posistion+nums-1
            mul+=1
        # result_list.append(sovling_list)
        n_add+=1
    result=""
    for list in result_list:
        result+=list+"\n"
    return result
            
           
a="PAYPALISasdasdHIRING"
nums=4
print(z_string_convert(a,nums)) 
  

