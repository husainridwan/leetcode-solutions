/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    const par = {"}":"{", "]":"[", ")":"("};
        for (let i of s) {
        if (i in par) {
            if (stack.length > 0 && stack[stack.length - 1] === par[i]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(i);
        }
    }
    return stack.length === 0;
};