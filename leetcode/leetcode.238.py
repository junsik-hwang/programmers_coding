# leetcode 238. Product of Array Except Self

nums = [1,2,3,4]
point = 1
out = []
for i in range(len(nums)):
    out.append(point)
    point = point * nums[i]

point = 1
for i in range(len(nums) - 1, -1, -1):
    out[i] *= point
    point *= nums[i]

print(out)