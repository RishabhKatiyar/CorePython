class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        temp1 = l1
        temp2 = l2
        carry = 0
        resultList = ListNode()
        temp = resultList
        while temp1 != None and temp2 != None:
            result = 0
            a = 0
            b = 0
            if temp1 != None:
                a = temp1.val
                temp1 = temp1.next
            if temp2 != None:
                b = temp2.val
                temp2 = temp2.next
            result =  a + b + carry
            carry = int(result / 10)
            print(carry)
            value = int(result % 10)
            temp.val = value
            print(value)
            if (temp1 != None and temp2 != None) or carry != 0:
                temp.next = ListNode()
            temp = temp.next
        return resultList


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ob = Solution()
    res = ob.addTwoNumbers(l1, l2)

    while res != None:
        print(f'{res.val} ->', end='\t')
        res= res.next
