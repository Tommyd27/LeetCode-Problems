def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-/*":
            r,l  = stack.pop(), stack.pop()
            print(f"{l} {token} {r}")
            out = int(eval(f"{l} {token} {r}"))
            stack.append(out)
        else:
            stack.append(int(token))
    return stack.pop()
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))