def isValid(s: str) -> bool:
    s = []
    for char in s:
        if char in "([{":
            s.append(char)
        else:
            prev_char = s.pop()
            if (prev_char == "(" and char == ")") or (prev_char == "[" and char == "]") or (prev_char == "{" and char == "}"):
                continue
            return False
    return False if s else True
print(isValid("(]"))