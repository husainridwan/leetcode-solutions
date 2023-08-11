/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    let answer = Array(boxes.length).fill(0);
    let notEmpty = 0;
    let runningTotal = 0;
    //Make one pass through the array (left to right), getting every move for each non-empty box
    //on the left of the current index by adding the previously seen nonempty boxes to the running total
    for(let i=0; i<boxes.length; ++i) {
        answer[i] += runningTotal;
        if(boxes[i] === '1') {
            ++notEmpty;
        }
        runningTotal += notEmpty;
    }
    //Make one more pass through the array (right to left).
    notEmpty = 0;
    runningTotal = 0;

    for(let i=boxes.length-1; i>=0; --i) {
        answer[i] += runningTotal;
        if(boxes[i] === '1') {
            ++notEmpty;
        }
       runningTotal += notEmpty;
    }
    return answer;
};