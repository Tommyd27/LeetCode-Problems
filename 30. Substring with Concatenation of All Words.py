def findSubstring(self, s: str, words: List[str]) -> List[int]:
	lenOfWord = len(words[0])
	lenOfWords = len(words)
	lenOfWindow = lenOfWords * lenOfWord
	lenOfStr = len(s)
	output = []
	checkDictionary = {}
	for word in words:
		if word in checkDictionary:
			checkDictionary[word] += 1
		else:
			checkDictionary[word] = 1
	wordStartIndexRange = range(lenOfWindow // lenOfWord)
	for startIndex in range(lenOfStr):
		#for word in words:
		#    if word in s[actualStartIndex : actualStartIndex + lenOfWindow]:
		#        continue
		#    valid = False
		#    break
		thisDictionary = {}
		valid = True
		for wordStartIndex in wordStartIndexRange:
			actualWordStartIndex = startIndex + wordStartIndex * lenOfWord
			strChunk = s[actualWordStartIndex : actualWordStartIndex + lenOfWord]

			try:
				thisDictionary[strChunk] += 1
			except KeyError:
				thisDictionary[strChunk] = 1
			if strChunk not in checkDictionary or thisDictionary[strChunk] > checkDictionary[strChunk]:
				valid = False
				break
		if valid:
			output.append(startIndex)
	return output
        

print(findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))