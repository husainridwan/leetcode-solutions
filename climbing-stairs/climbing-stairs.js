/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let cache = {};
    function climb(num) {
        if (num in cache) {
            return cache[num];
        }    
        let result = 0;
        if(num <= 3) {
            result = num;
        } else if (n>3) {
            result = climb(num-1) + climb(num-2);
        }
        
        cache[num] = result;
        return result;
    }
    
    return climb(n);
};