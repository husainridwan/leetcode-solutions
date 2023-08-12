/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function(nums, k) {
    const indexedNums = nums.map((num, index) => [num, index]); // Map each number to its index
    indexedNums.sort((a, b) => b[0] - a[0]); // Sort the mapped array in descending order based on the numbers
    // Get the first k elements and sort them back based on the indexes
    const result = indexedNums.slice(0, k).sort((a, b) => a[1] - b[1]);
    // Extract only the numbers from the result
    const subsequence = result.map(([num, _]) => num);
    return subsequence;

}