/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let dp = new Array(grid.length).fill(0).map(() => new Array(grid[0].length).fill(0));
    dp[0][0] = grid[0][0];

    for(let i=1; i<grid.length; i++) {
        dp[i][0] = dp[i-1][0] + grid[i][0];
    }

    for(let j=1; j<grid[0].length; j++) {
        dp[0][j] = dp[0][j-1] + grid[0][j];
    }

    for(let i=1; i<grid.length; i++) {
        for(let j=1; j<grid[0].length; j++) {
            dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
        }
    }

    return dp[grid.length-1][grid[0].length-1];
};