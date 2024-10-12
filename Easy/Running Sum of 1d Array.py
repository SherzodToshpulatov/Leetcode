#https://leetcode.com/problems/running-sum-of-1d-array/description/
def runningSum(nums):
    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i-1]

    return nums

a = [1,2,3,4]
print(runningSum(a))


