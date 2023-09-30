# def find_longesr_reversiable_string(a):
   
#     result=a[0]
#     result_max=""
#     for current_position in range(len(a)):
#        mid_point=current_position+1
#        repeat_time=1
#        edge=0
#        print("loop",current_position)
#        while True:
#          if mid_point+1>len(a)-1:
#                 print ("early break mid point:",mid_point)
#                 print ("break early")
#                 break
#          else:
#              if a[mid_point]==a[mid_point+1]:
#                  result=a[mid_point-repeat_time:mid_point+1+1]
#                  mid_point+=1
#                  repeat_time+=1
#              elif a[mid_point-repeat_time-edge]==a[mid_point+edge+1]:
#                  print ("repeat_time",repeat_time)
#                  print ("mid_point",mid_point)
#                  print ("edge",edge)
#                  result=a[mid_point-repeat_time-edge:mid_point+edge+1+1]
#                  edge+=1
#                  print ("result",result)
#                  if mid_point+edge==len(a)-1:
#                      break
#              if len(result)>len(result_max):
#                  result_max=result
#        if mid_point+1==len(a)-1:
#               break 
#     return result_max
### use two function to solve the problem, above code only uses one function, which is too complicated
def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)           # odd
        len2 = expand_around_center(s, i, i + 1)       # even
        max_len = max(len1, len2)

        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]

def expand_around_center(s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

a = "aaba"
print(longest_palindrome(a))

