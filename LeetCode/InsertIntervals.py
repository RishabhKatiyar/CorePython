class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #insert new interval in existing list
        length = len(intervals)
        if length == 0:
            return [newInterval]
        '''
        i = 0
        while i < length:
            if not intervals[i][0] < newInterval[0]:
                break
            i += 1
        intervals.insert(i, newInterval)
        print(intervals)
        '''
        #shrink intervals
        count = 0
        for interval in intervals:
            if interval[0] <= newInterval[0] and newInterval[0] <= interval[1]:
                break
            count += 1
        print(count)
        interval = intervals[count]
        print(interval)
        

intervals = [[1,3],[6,9]]
newInterval = [2,5]
#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#newInterval = [4,8]
#intervals = [[1,5]]
#newInterval = [2,3]
#intervals = [[1,5]]
#newInterval = [2,7]
#intervals = []
#newInterval = [5,7]
ob = Solution()
print(ob.insert(intervals, newInterval))