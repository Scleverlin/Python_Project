a="aaszxcvadb"
# print (a[0])

def find_no_overlap_string(a):
    iteration = 0
    result_list = []
    tmp_list = []

    while iteration < len(a):
        char = a[iteration]
        if char in tmp_list:
            result_list.append(len(tmp_list))
            # print (tmp_list)
            tmp_list = []
            iteration -= len(tmp_list)-1
        else:
            tmp_list.append(char)
            iteration += 1
        if iteration == len(a):
            result_list.append(len(tmp_list))
            print (tmp_list)
            break

    return max(result_list) if result_list else 0

print(find_no_overlap_string(a))

       
           
            
            
    
        
    