/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (!nums.includes(target)) {
        return -1;
    }
    
    let l = 0;
    let r = nums.length - 1;
    
    while (l <= r) {
        let mid = Math.floor(l + (r - l) / 2);
        
        if (target === nums[mid]) {
            return mid;
        }
        
        if (nums[mid] <= nums[r]) {
            if (target > nums[mid] && target <= nums[r]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        } else {
            if (target < nums[mid] && target >= nums[l]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
    } 
    return -1;
};