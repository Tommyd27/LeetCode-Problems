
def findTarget(root, k: int) -> bool:
	prevNodes = []
	def helper(root):
		if not root:
			return False
		cTarget = k - root.val
		if cTarget in prevNodes:
			return True
		prevNodes.append(root.val)
		if cTarget > root.val:
			if helper(root.right): return True
			if helper(root.left): return True
		elif root.left:
			if helper(root.left): return True
			if helper(root.right): return True
		return False
	return helper(root)
findTarget(, -3)