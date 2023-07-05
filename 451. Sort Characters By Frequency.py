from collections import Counter
def frequencySort(s: str) -> str:
	c = Counter(s)
	s = list(s)
	s.sort(reverse = True, key = lambda x : c[x])
	return "".join(s)
print(frequencySort("tree"))