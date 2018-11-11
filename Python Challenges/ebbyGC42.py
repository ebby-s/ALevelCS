import random

def avg(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)

rand_nums = [random.randint(0,255) for i in range(50)]
print(rand_nums)
print(min(rand_nums))
print(max(rand_nums))
print(avg(rand_nums))
