class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        visited=set()
        for i in range(n):
            if nums[i] in visited:
                return True
            elif nums[i] not in visited:
                visited.add(nums[i])
        return False