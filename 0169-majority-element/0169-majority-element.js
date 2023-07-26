/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const myMap = new Map();
    let highest = 0;
    let most = 0;
    
    for(let el of nums) {
        if(myMap.has(el)) {
            myMap.set(el, myMap.get(el)+1);
        } else {
            myMap.set(el, 1);
        }
        
        if(highest < myMap.get(el)) {
            highest = myMap.get(el);
            most = el;
        }
    }
    return most;
};