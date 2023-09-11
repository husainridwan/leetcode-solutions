/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let result = new Array(digits.length-1).fill(0);
    let intArr = BigInt(digits.join(""));
    let intStr = String(intArr + BigInt(1));

    for(let i=intStr.length-1; i >= 0; i--) {
        result[i] = Number.parseInt(intStr[i]);
    }
    return result;  
};