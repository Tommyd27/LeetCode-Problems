lst = [1, 3, 10, 15, 23, 140, 141]

def bisect(val):
	l, r = 0, len(lst)

	while l < r:
		mid = (l + r) // 2
		if lst[mid] == val:
			r = mid
			break
		elif lst[mid] > val:
			r = mid
		else:
			l = mid + 1
	return l, r, mid
lst.insert()
print(bisect(140))