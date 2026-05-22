class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and abs(i-j)<=k :
                    
                        count+=1
                    
                        
        if count>0:
            return True
        else:
            return False