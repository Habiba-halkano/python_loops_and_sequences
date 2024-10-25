#write a python function using a loop that returns the sum of all numbers in the given list

def sum_list():
    nums = [1, 2, 3, 4, 5]
    total = 0
    num = 0
    while num < len(nums):
         total = total + nums[num]
         num = num + 1
    print(total)

sum_list()