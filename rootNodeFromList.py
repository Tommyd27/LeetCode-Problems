binaryTree = [4,2,None,-3,None,None,-1,None,0]

class Node:
	def __init__(self, val, left = None, right = None) -> None:
		self.val = val
		self.left = left
		self.right = right

def insertLevelOrder(arr, i, n):
    root = None
    # Base case for recursion 
    if i < n:
        root = Node(arr[i]) 
		if not root:
			return root
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1, n)
  
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2, n)
          
    return root
root = insertLevelOrder(binaryTree, )
