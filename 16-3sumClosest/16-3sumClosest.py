# Last updated: 6/2/2026, 12:05:20 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > target:
                    res.append((total,total-target))
                    k -= 1
                elif total < target:
                    res.append((total,target-total))
                    j += 1
                else:
                    return target
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        sorted_res = sorted(res, key=lambda x: x[1])
        return sorted_res[0][0]