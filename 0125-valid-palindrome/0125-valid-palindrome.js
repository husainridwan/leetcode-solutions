/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // let palStr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    // const myMap = new Map();
    // for(const el of palStr) {
    //     if(myMap.has(el)) {
    //         myMap.delete(el);
    //     } else {
    //         myMap.set(el, 1);
    //     }
    // }
    // return myMap.size <= 1;
    let palStr = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    let reversedStr = palStr.split("").reverse().join("");
    return palStr === reversedStr;
};