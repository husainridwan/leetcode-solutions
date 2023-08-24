/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let size = matrix.length
    //Transpose the matrix
    for (let i=0; i<size; i++) {
        for (let j=0; j<i; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    //Reverse the result
    for (let i=0; i<size; i++) {
        matrix[i].reverse();
    }
};