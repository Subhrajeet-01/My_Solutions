class Solution(object):
    def search(self, nums, target):
        start,end = 0,len(nums)-1
        for i in range(len(nums)):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            else:
                if target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
