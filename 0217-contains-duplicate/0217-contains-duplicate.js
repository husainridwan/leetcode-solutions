/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let myMap = new Map();
    for(const el of nums) {
        if(myMap.has(el)) {
            return true;
        } else {
            myMap.set(el, 1);
        }
    }
    return false;
};