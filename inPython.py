# LEETCODE PROBLEM- TWO SUM (https://leetcode.com/problems/two-sum/submissions/1305905993/)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        for j in range (len(nums)-1):
            for i in range(j+1,len(nums)):
                if nums[j]+nums[i]==target:
                    a.append(j)
                    a.append(i)
                    break
        return a
