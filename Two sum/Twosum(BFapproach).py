class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i] == target:
                    l.append(i)
                    l.append(j)
                else:
                    j=j+1
        return l
