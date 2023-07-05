



def sortedArrayToBST(nums):
    bsT = []

    numsLen = len(nums)
    sizeOfRow, numOfRows = 1, 0
    midpoint = numsLen // 2
    dFromMid = 0
    while numsLen > numOfRows:
        for i in range(sizeOfRow):
            if i >= sizeOfRow / 2:
                try:
                    bsT.append(nums[midpoint + dFromMid])
                except IndexError:
                    bsT.append(None)
            else:
                indexToTry = midpoint - dFromMid
                if indexToTry >= 0:
                    bsT.append(nums[midpoint - dFromMid])
                else:
                    bsT.append(None)
            if not i % 2 and i:
                dFromMid += 1
        dFromMid += 1
        numOfRows += sizeOfRow
        sizeOfRow *= 2
    return bsT
#[0,-3,9,-10,null,5]
print(sortedArrayToBST([-10,-3,0,5,9]))