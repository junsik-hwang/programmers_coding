# leetcode 1. Two Sum

nums = [2, 7, 11, 15]
target = 9

for i, n in enumerate(nums):
    ans = target - n

    if(ans in nums[i + 1:]):
        print(nums.index(n), nums[i+1:].index(ans) + (i + 1))