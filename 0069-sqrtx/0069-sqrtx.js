/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let left = 0, right=x, ans = 0; 
    while (left<=right){ 
        let mid = Math.floor((left+right)/2); 

        if (mid*mid == x){ 
            return mid; 
        } else if (mid*mid < x) {
            ans = mid; //  
            left = mid + 1; // Updating the left pointer/
        } else {
            right = mid - 1; // if mid*mid is greater then we will update the right pointer
        }
    }
    return ans; // if we never encountered `mid*mid == x` then we will return our answer variable.
};