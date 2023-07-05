def bagOfTokensScore(tokens: list[int], power: int) -> int:
	tokens.sort()
	score = 0

	for i, token in enumerate(tokens):
		if token <= power:
			power -= token
			score += 1
		else:
			while power < token:
				lenToken = len(tokens) 
				if lenToken - i > 1 and score > 0:
					power += tokens.pop()
					score -= 1
				else:
					return score
			power -= token
			score += 1
	return score

print(bagOfTokensScore([17,47,41,57,51], 31))
	