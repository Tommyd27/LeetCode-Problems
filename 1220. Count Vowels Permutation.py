"""Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 

Input: n = 5
Output: 68

 

Constraints:

    1 <= n <= 2 * 10^4

"""

from time import time
from math import pow
modular = pow(10, 9) + 7
def SolutionControl(n : int) -> int:
    nextLetterDictionary = { #dictionary of, for each letter, what are valid next characters that can be entered
        "a" : ["e"],
        "e" : ["a", "i"],
        "i" : ["a","e","o","u"],
        "o" : ["i","u"],
        "u" : ["a"]
    }
    depthCache = {
        "a" : {0 : 1},
        "e" : {0 : 1},
        "i" : {0 : 1},
        "o" : {0 : 1},
        "u" : {0 : 1}
        }
    def FindNumLetters(previousLetter, depth, currentCount = 0):
        try:
            currentCount += depthCache[previousLetter][n - depth]
        except KeyError:
            newCount = 0
            for letter in nextLetterDictionary[previousLetter]:#go through every other possible letter
                newCount = FindNumLetters(letter, depth + 1, newCount)#increase depth by one
            depthCache[previousLetter][n - depth] = newCount
            currentCount += newCount
        if depth == 2:
            pass
        return currentCount  
    count = 0
    for letter in nextLetterDictionary:
        count += FindNumLetters(letter, 1)
    return count

def SolutionOptimised(n : int) -> int:
    dp = [[1] * 5]
    for _ in range(n - 1):
        dp += [[0] * (5)]
        #a
        dp[-1][0] = dp[0][1] + dp[0][2] + dp[0][4]
        #e
        dp[-1][1] = dp[0][0] + dp[0][2]
        #i
        dp[-1][2] = dp[0][1] + dp[0][3] 
        #o
        dp[-1][3] = dp[0][2]
        #u
        dp[-1][4] = dp[0][2] + dp[0][3]

        del dp[0]
    return sum(dp[0])
def SolutionOptimisedModular(n : int) -> int:#has modular thingy that site wants
    a, e, i, o, u = [1] * 5
    for _ in range(n - 1):
        a, e, i, o, u = map(lambda x : x % modular, [e + i + u, a + i, e + o, i, i + o])
    return int((a + e + i + o + u) % modular)
def SolutionOptimisedModularTwo(n : int) -> int:
    a, e, i, o, u = [1] * 5
    for _ in range(n - 1):
        a, e, i, o, u = (e + i + u) % modular, (a + i) % modular, (e + o) % modular, (i) % modular, (i + o) % modular
    return int((a + e + i + o + u) % modular)


#Optimisation
n = 1000000

"""start = time()
print(f"Control: {SolutionControl(n)}")
end = time()
print(f"Control Time: {end - start}")


start = time()
print(f"Optimised: {SolutionOptimised(n)}")
end = time()
print(f"Optimised Time: {end - start}")
"""


start = time()
print(f"Optimised: {SolutionOptimisedModular(n)}")
end = time()
print(f"Optimised Time: {end - start}")

start = time()
print(f"Optimised: {SolutionOptimisedModularTwo(n)}")
end = time()
print(f"Optimised Time: {end - start}")




