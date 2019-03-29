#coding:utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        
        for i in nums:
            for j in nums :
                if i + j == target:
                    re = []
                    if nums.index(i) not in re and nums.index(j)not in re :
                        #list(set(re))
                        re.append(nums.index(i))
                        re.append(nums.index(j))
                        return re
                else:
                    pass

                    
if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9
    print Solution().twoSum(nums,target)
