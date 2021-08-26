class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:] #convert to binary number
        n = '%32s' % n #add extra spacing
        n = n.replace(' ','0') #converting the space into zero
        return int(n[::-1],2) #printing the reverse integer value 

#n = 00000010100101000001111010011100
n = 43261596
ob = Solution()
print(ob.reverseBits(n))