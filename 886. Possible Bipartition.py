def possibleBipartition(n: int, dislikes: list[list[int]]) -> bool:
    set1 = set()
    set2 = set()
    for a, b in dislikes:
        if a in set1:
            if b in set1:
                return False
            set2.add(b)
        elif a in set2:
            if b in set2:
                return False
            set1.add(b)
        elif b in set1:
            set2.add(a)
        elif b in set2:
            set1.add(a)
        else:
            set1.add(a)
            set2.add(b)
    return True
print(possibleBipartition(10, [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]))