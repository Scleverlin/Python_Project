
def chain_adder(a,b):
   max_list= max(a, b, key=len)
   min_list = min(a, b, key=len)
   result_list=[]
   carry=0
   for i in range(len(max_list)):
      if i> (len(min_list)-1):
         min_list.append(0)
      result_list.append((max_list[i]+min_list[i]+carry)%10)
      carry= max_list[i]+min_list[i]+carry>9
   return result_list

a=[1,2,3,4,5]
b=[1,2,3,4,5,6,7,8,9]
print(chain_adder(a,b))
      
      
         