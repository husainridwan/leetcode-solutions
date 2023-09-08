/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let left = 0;
    let right = s.length - 1;
    
    function helper(left, right) { // Feeling like Timi
        if (left >= right) {
            return;
        }
        
        const temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        
        helper(left+1, right-1);
    }
    helper(left, right);
    return;
};