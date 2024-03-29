Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output=[]
        
        def dfs(node):
            if not node:
                return 
            output.append(node.val)
            
            for c in node.children:
                dfs(c)
            
        dfs(root)
        
        return output
