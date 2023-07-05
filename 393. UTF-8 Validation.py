def validUtf8(data: list[int]) -> bool:
	binData = ["{:08b}".format(x) for x in data]
	binDataSplit = []
	i = 0
	dataLen = len(binData)
	while i < dataLen:
		primaryBlob = str(binData[i])
		if primaryBlob[0] == "0":
			i += 1
			continue
		try:
			sizeOfBlob = primaryBlob.index("0")
			if 1 == sizeOfBlob or sizeOfBlob > 4:
				return False
		except ValueError:
			return False
		if i + sizeOfBlob > dataLen:
			return False
		binDataSplit.append(binData[i : i + sizeOfBlob])
		i += sizeOfBlob
	for chunk in binDataSplit:
		for secondaryChunk in chunk[1:]:
			if "10" != str(secondaryChunk)[:2]:
				return False
	return True
print(validUtf8([250,145,145,145,145]))
		