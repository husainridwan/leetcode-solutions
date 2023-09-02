/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
    function dfs(node, max) {
        if (!node) {
            return 0;
        }
        let left = Math.max(0, dfs(node.left, max));
        let right = Math.max(0, dfs(node.right, max));
        max.val = Math.max(max.val, left + right + node.val);
        return Math.max(left, right) + node.val;
     }
    let max = { val: -Infinity };
    dfs(root, max);
    return max.val;
};