class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        l=[]
        for i in range(len(nums)):
            rem=target - nums[i]
            if rem in seen:
                l.extend([seen[rem],i])
            else:
                seen[nums[i]]=i
        return l
