# Nada Bencheikh (nb5xu)
# problem 217 contains duplicates 

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        else:
            for i in range(len(nums)):
                for j in range(len(nums)):

                    if nums[i]==nums[j] and i!=j:
                        return True
            return False