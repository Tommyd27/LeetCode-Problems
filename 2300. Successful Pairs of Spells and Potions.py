def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    potions.sort()
    m = len(potions)
    for i, spell in enumerate(spells):
        low, high = 0, m
        while low < high:
            mid = (low + high) // 2
            product = spell * potions[mid]
            if product < success:
                low = mid + 1
            else:
                high = mid
        spells[i] = low
    return spells
print(successfulPairs([5,1,3], [1,2,3,4,5], 7))

#4, 0, 3