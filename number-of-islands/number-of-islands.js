/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if (grid.length === 0) {
        return 0;
    }
  
    let count = 0;
  
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] === '1') {
                count++;
            dfs(grid, i, j);
            }
        }
    }
    return count;
}

function dfs(grid, x, y) {
    if (x < 0 || x >= grid.length || y < 0 || y >= grid[x].length || grid[x][y] !== '1') {
        return;
    }
  
    grid[x][y] = '0';
  
    dfs(grid, x + 1, y);
    dfs(grid, x - 1, y);
    dfs(grid, x, y + 1);
    dfs(grid, x, y - 1);
};