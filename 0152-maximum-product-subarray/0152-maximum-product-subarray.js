/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let a = nums[0];
    let b = nums[0];
    let result = nums[0];
    
    for (let i=1; i<nums.length; i++) {
        let temp = a;
        a = Math.max(nums[i], Math.max(a*nums[i], b*nums[i]));
        b = Math.min(nums[i], Math.min(temp*nums[i], b*nums[i]));
        result = Math.max(result, a);
    }
    
    return result;
};