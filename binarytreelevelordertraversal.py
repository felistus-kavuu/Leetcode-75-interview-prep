Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        q= collections.deque()
        q.append(root)
        
        while q:
            l= len(q)
            ans=[]
            for i in range(l):
                node= q.popleft()
                if node:
                    ans.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if ans:
                result.append(ans)
        
        return result
        
