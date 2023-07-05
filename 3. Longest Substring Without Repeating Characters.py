def lengthOfLongestSubstring(s: str) -> int:
	strLen = len(s)
	longest = 0
	count = 0
	for i in range(strLen):
		section = ""
		count = 0
		for char in s[i:]:
			if char not in section:
				section += char
				count += 1
			else:
				if count > longest:
					longest = count
				break
		else:
			break
	if count > longest:
		return count
	return longest
print(lengthOfLongestSubstring("au"))