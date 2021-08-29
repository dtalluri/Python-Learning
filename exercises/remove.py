def removeElement(self, nums, val):
    x = len(nums)
    i = 0
    while i < x:
        if nums[i] == val:
            del nums[i]
            x = x-1
            i = i - 1
        i = i+1
