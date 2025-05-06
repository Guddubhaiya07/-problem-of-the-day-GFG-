class Solution:
    def LeftView(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
if __name__ == "__main__":
    
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = LeftView(root)
    for val in result:
        print(val, end=" ")
    print()
