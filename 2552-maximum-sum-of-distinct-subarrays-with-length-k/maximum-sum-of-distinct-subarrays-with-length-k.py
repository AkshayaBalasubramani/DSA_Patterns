class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        curr_sum=0
        max_sum=0
        left=0
        window=set()

        right=0

        while right<len(nums):
            while(nums[right] in window) or (len(window)==k):
                window.remove(nums[left])
                curr_sum=curr_sum-nums[left]
                left+=1
            
            curr_sum+=nums[right]
            window.add(nums[right])
            if len(window)==k:
                max_sum=max(curr_sum,max_sum)
            right+=1

        return max_sum


