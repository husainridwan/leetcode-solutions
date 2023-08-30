/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let l = 0;
    let r = height.length - 1;
    let maxWater = 0;
    
    while (l < r) {
        let width = r - l;
        let area = Math.min(height[l], height[r]) * width;
        maxWater = Math.max(maxWater, area);
        
        if (height[l] <= height[r]) {
            l += 1;
        }else {
            r -= 1;
        }
    }
    return maxWater;
};