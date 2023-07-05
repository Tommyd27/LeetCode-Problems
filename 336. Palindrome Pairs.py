def palindromePairs(words: list[str]) -> list[list[int]]:
	backwardsWords = {words[x][::-1] : x for x in range(len(words))}
	output = []
	
	
	for i, word in enumerate(words):
		if word in backwardsWords and backwardsWords[word] != i:
			output.append([i, backwardsWords[word]])
			
		if word != "" and "" in backwardsWords and word in backwardsWords:
			output += [[i, backwardsWords[""]], [backwardsWords[""], i]]
		
		for j in range(len(word)):
			wordFromJ = word[j:]
			wordUpToJ = word[:j]

			wordFromJBackwards = word[j-1 :: -1]
			wordUpToJBackwards = word[:j - 1: -1]
			pass
			if wordFromJ in backwardsWords and wordUpToJ == wordFromJBackwards:
				output.append([backwardsWords[wordFromJ], i])
			if wordUpToJ in backwardsWords and wordFromJ == wordUpToJBackwards:
				output.append([i, backwardsWords[wordUpToJ]])
	return output


words = ["abcd","dcba","lls","s","sssll"]

palindromePairs(words)