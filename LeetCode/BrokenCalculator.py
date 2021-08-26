from queue import Queue
class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        my_set = set()
        queue = Queue()
        queue.put([x, 0])
        my_set.add(x)
        while True:
            item = queue.get()
            val = item[0]
            level = item[1]
            if val == y:
                break
            double = val * 2
            decrement = val - 1
            if not double in my_set and double <= 1000000000:
                my_set.add(double)
                queue.put([double, level+1])
            if not decrement in my_set:
                my_set.add(decrement)
                queue.put([decrement, level+1])

        return level


ob = Solution()
print(ob.brokenCalc(2,3))
print(ob.brokenCalc(1024,1))
