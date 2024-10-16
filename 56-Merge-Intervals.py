class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            inter = intervals[i]
            if res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1],inter[1])
            
        return res

        