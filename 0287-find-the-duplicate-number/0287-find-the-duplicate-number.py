class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #check = {}
        
        #for num in nums:
        #    if num not in check:
        #        check[num] = 1
        #    else:
        #        return num
        nums.sort()
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r)//2
            if  (mid == 0 or nums[mid] == nums[mid-1]) or (mid == len(nums)-1 or nums[mid] == nums[mid+1]):
                return nums[mid]
            else:
                if r-mid > nums[r]-nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1