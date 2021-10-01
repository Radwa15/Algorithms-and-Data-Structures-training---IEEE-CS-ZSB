class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(0,len(nums)):
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] == target:
                        temp = sorted([nums[i], nums[j], nums[left], nums[right]])
                        res.append((temp[0], temp[1], temp[2], temp[3]))
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        
        return set(res)
