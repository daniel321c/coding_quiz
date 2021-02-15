import sys
def findPeakElement(nums):

    if(len(nums) == 1):
        return 0

    intMin = -sys.maxsize - 1

    if(nums[0] > intMin and nums[0] > nums[1]):
        return 0

    for i in range(1, len(nums)-1):

        if(nums[i] > nums[i-1] and nums[i] > nums[i+1]):
            return i

    print(nums[-1], nums[-2])
    if(nums[-1] > intMin and nums[-1] > nums[-2]):
        return len(nums)-1


print(findPeakElement([1, 2]))

k= [[2, 1],[1, 3]]
k.sort(key = lambda x : x[0])
print(k)