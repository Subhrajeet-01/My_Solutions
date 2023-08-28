class Solution(object):
    def findKthLargest(self, nums, k):
        
        maxHeap = [-ele for ele in nums]
        heapq.heapify(maxHeap)

        while k:
            ans = -heapq.heappop(maxHeap)
            k -= 1
        return ans
