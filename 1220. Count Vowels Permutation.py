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

def Solution(n : int) -> int:
    nextLetterDictionary = { #dictionary of, for each letter, what are valid next characters that can be entered
        "a" : "e",
        "e" : "ai",
        "i" : "aeou",
        "o" : "iu",
        "u" : "a"
    }
    def FindNumLetters(previousLetter, depth, currentCount = 0):
        if depth == n:#if length is correct
            currentCount += 1 #new variation, so add one
        else:
            for letter in nextLetterDictionary[previousLetter]:#go through every other possible letter
                currentCount = FindNumLetters(letter, depth + 1, currentCount)#increase depth by one
        return currentCount   
    count = 0
    for letter in nextLetterDictionary:
        count += FindNumLetters(letter, 1)
    return count

for n in range(1, 10):
    print(f"{n} : {Solution(n)}")