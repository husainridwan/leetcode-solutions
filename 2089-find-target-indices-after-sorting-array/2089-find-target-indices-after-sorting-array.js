/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let hash = [];
    nums.sort((a, b) => a - b);
    
    nums.forEach((num, idx) => {
        if(num === target)
            hash.push(idx);
        });
    return hash;
};