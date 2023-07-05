from collections import defaultdict
def numberOfWeakCharacters(properties: list[list[int]]) -> int:
	champStrengths = defaultdict(list)
	highestDefenseStrengthValue = {}
	
	for champ in properties:
		champStrengths[champ[0]].append(champ[1])
	highestStrengthValue = max(champStrengths.keys())
	weakChamps = 0
	for strengthValue in champStrengths.keys():
		for champ in champStrengths[strengthValue]:
			for higherStrengthValue in range(highestStrengthValue - strengthValue):
				sStrength = strengthValue + higherStrengthValue
				if sStrength in highestDefenseStrengthValue:
					highestDef = highestDefenseStrengthValue[sStrength]
				else:
					try:
						highestDef = max(champStrengths[sStrength])
					except ValueError:
						highestDef = 0
					highestDefenseStrengthValue[sStrength] = highestDef
				if highestDef > champ:
					weakChamps += 1
					break
	return weakChamps

print(numberOfWeakCharacters([[2,2],[3,3]]))