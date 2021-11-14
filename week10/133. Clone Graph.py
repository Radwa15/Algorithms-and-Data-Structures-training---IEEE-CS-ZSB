class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        vist= {}
        def helper(node):
            if node:
                cp= Node(node.val)
                vist[node]=cp

                for neighbor in node.neighbors:      
                    if neighbor in vist: 
                        cp.neighbors.append(vist[neighbor])
                    else: 
                        cp.neighbors.append(helper(neighbor))
               
                return cp
        
        rst =  helper(node)
        return rst
