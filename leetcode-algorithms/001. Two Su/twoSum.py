class Solution1:
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