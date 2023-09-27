import re

text = "a123b asdasda4567b"
matches = re.findall(r'a(.*?)b', text)
print(matches)  # 输出: ['123', '4567']


def find_targer_sum_dict(list,target): # using dictionary # right now it is not working
    seen={}
    for i,nums in enumerate (list):
        complement_of_tar = target - nums
        if complement_of_tar in seen:
            return [seen[complement_of_tar], i]
        seen[nums] = i
    return []

a=find_targer_sum_dict([2,11,7,15],9)
print(a)