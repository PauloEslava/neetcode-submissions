class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        result = []

        for i in range(0, len(nums)):
            
            # If we encounter a duplicate, we skip over to the next iteration
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now we check for the possible number pairs so that n1 + n2 = -ni
            left = i + 1
            right = len(nums) - 1
            

            while left < right:
                
                current_sum = nums[left] + nums[right]
                
                if current_sum == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < -nums[i]:
                    left += 1
                else:
                    right -= 1

        return result