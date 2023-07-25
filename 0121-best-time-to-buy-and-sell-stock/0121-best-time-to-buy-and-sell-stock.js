/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0;
    let r = 1;
    let maxProfit = 0;
    
    while(r < prices.length) {
        if(prices[l] < prices[r]) {
            profit = prices[r] - prices[l];
            maxProfit = Math.max(maxProfit, profit)
        } else {
            l = r;
        }
        r += 1;
    }
    return maxProfit;
};