
class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        nums_len = len(nums)
        for i in range(nums_len):
            dif = target - nums[i]
            if dif in nums_hash: 
                return [nums_hash[dif], i]
            nums_hash[nums[i]] = i
        return []

class Solution2:
    def twoSum(self, nums, target):
        boo = False
        lenNums = len(nums)
        for i in range(lenNums-1):
            for j in range(i+1,lenNums):
                sum = nums[i] + nums[j]
                if sum == target:
                    boo = True
                    break
            if boo:
                break
        return [i,j]
        
        
if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 3
    print(Solution1().twoSum(nums, target))
    print(Solution2().twoSum(nums, target))