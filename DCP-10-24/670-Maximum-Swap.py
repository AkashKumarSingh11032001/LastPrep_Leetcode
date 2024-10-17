class Solution:
    def maximumSwap(self, num: int) -> int:
        # split number into list
        # sort it, and find max from [1:]
        #compare from max with sorted list[0]
        #if greater swap it else return the same number
        maxIdx = -1
        max_dig = \0\
        swap1 = -1
        swap2 = -1
        numList = list(str(num))
        # print(numList)
        for i in reversed(range(len(numList))):
            if numList[i] > max_dig:
                maxIdx = i
                max_dig = numList[i]
            if numList[i] < max_dig:
                swap1 = i
                swap2 = maxIdx
        
        numList[swap1], numList[swap2] = numList[swap2], numList[swap1]
        return int(''.join(numList))
        