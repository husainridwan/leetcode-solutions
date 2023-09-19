/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findBall = function(grid) {
    let result = [];
    for(let i=0; i<grid[0].length; i++) {
        result.push(findBallHelper(grid, 0, i));
    }
    return result;
    
    function findBallHelper(grid, row, col) {
        if(row === grid.length) {
            return col;
        }
        
        if(grid[row][col] === 1) {
            if(col === grid[0].length-1 || grid[row][col+1] === -1) {
                return -1;
            }
            return findBallHelper(grid, row+1, col+1);
        } else {
            if(col === 0 || grid[row][col-1] === 1) {
                return -1;
            }
            return findBallHelper(grid, row+1, col-1);
        }
    }
    
};

