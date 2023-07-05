def numDecodings(s): 
	if not s:
		return 0
	lenS = len(s)
	dp = [0 for _ in range(lenS + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, lenS + 1): 
		# One step jump
		one = int(s[i-1:i])
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		two = int(s[i-2:i])
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[lenS]

testCases = ["12", "226", "06"]
for case in testCases:
	numDecodings(case)