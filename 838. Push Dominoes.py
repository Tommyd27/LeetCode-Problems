from xml import dom


def pushDominoes(dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]
        domList = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for p in range(i+1 , j):
                    domList[p] = x
            elif x == "R":
                midpoint = (j + i) / 2
                for l in range(i + 1 , j):
                    if l < midpoint:
                        domList[l] = "R"
                    elif l == midpoint:
                        domList[l] = "."
                    else:
                        domList[l] = "L"
        return ''.join(domList)
                
            
    


print(pushDominoes(".L.R."))
            
            