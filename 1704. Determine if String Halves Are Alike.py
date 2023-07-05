from collections import defaultdict
def halvesAreAlike(s: str) -> bool:
	c = defaultdict(int)
	mid = len(s) / 2
	vowels = ["a", "e", "i", "o", "u"]
	for i, char in enumerate(s):
		char = char.lower()
		if char in vowels:
			if i >= mid:
				c[char] += 1
			else:
				c[char] -= 1
	return max(c.values(), key = lambda x: abs(x)) == 0
print(halvesAreAlike("AbCdEfGh"))