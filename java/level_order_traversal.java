/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null){
            return ans;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        
        q.add(root);
        while (q.size() > 0){
            int n = q.size();
            ArrayList<Integer> curLevel = new ArrayList<>();

            for (int i = 0; i < n; i++){
                TreeNode cur = q.remove();
                curLevel.add(cur.val);
                if (cur.left != null){
                    q.add(cur.left);
                }
                if (cur.right != null){
                    q.add(cur.right);
                }
            }
            ans.add(curLevel);
        }

        return ans;
    }
}