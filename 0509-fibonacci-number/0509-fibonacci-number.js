/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    cache = {};
    function rec_fib(num) {
        if (num in cache) {
            return cache[num];
        }
        let result = 0;
        if (num < 2) {
            result = num;
        } else {
            result = rec_fib(num-1) + rec_fib(num-2);
        }
        
        cache[num] = result;
        return result;
    }
    
    return rec_fib(n);
};