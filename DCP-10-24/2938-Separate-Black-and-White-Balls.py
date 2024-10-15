class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt,black = 0,0
        for i in s:
            if i=='0':cnt += black
            else:black += 1
        return cnt
        