class Solution:
    
    def knightDialer(self, n: int) -> int:
        next_dial=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        result = 0
        stack = []
        memo = {}
        if n == 1:
            return 10
        n -= 2
        stack.append((0, n))
        stack.append((1, n))
        stack.append((2, n))
        stack.append((3, n))
        stack.append((4, n))
        stack.append((6, n))
        stack.append((7, n))
        stack.append((8, n))
        stack.append((9, n))

        while len(stack):
            item = stack.pop()
            dialed_number = item[0]
            n = item[1]

            if str(dialed_number) + " " + str(n) in memo:
                result += memo[str(dialed_number) + " " + str(n)]
                continue

            if n == 0:
                result += len(next_dial[dialed_number])

            else:
                for next in next_dial[dialed_number]:
                    stack.append((next, n-1))

        return result % 1000000007

    def func(self, dialed_number: int, n: int) -> int:
        if n == 0:
            self.result += len(self.next_dial[dialed_number])
        else:
            for next in self.next_dial[dialed_number]:
                self.func(next, n-1)

ob = Solution()
print(ob.knightDialer(1))
print(ob.knightDialer(2))
print(ob.knightDialer(3))
print(ob.knightDialer(4))
print(ob.knightDialer(5))
print(ob.knightDialer(100))