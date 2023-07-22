/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    nums.sort((a, b) => a - b);
    let hash = [];
    for(let i=0; i<nums.length; i++) {
        if(nums[i] === target) {
            hash.push(i);
        }
    }
    return hash;
};