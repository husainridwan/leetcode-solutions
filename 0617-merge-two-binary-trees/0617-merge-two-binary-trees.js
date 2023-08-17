/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function(root1, root2) {
    if (!root1 && !root2) {
        return null;
    }
    if (!root1) {
        return root2;
    }
    if (!root2) {
        return root1;
    }
    
    let mergedTree = new TreeNode(root1.val + root2.val);
    mergedTree.left = mergeTrees(root1.left, root2.left);
    mergedTree.right = mergeTrees(root1.right, root2.right);
    
    return mergedTree;
};