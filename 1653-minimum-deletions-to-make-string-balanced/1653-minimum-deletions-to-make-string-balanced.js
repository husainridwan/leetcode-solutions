/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    let stack = [];
    let deletions = 0;
    
    for (let i = 0; i < s.length; i++) {
      if (s[i] === 'a') {
        if (stack.length > 0 && stack[stack.length-1] === 'b') {
          stack.pop(); // Matched 'a' with a previous 'b', remove b
          deletions++; // No previous 'b' to match with 'a', increase deletions
        }
      } else {
        stack.push('b'); // Encountered 'b', increase stack
      }
    }
    return deletions;
};