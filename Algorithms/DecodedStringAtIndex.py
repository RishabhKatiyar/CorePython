class Solution:
    def decodeAtIndex(self, s, k):
        result = '-1'
        
        # creating meta data
        length_of_s = len(s)
        start = 0
        end = 0
        meta_data = []
        meta_data.append([0, 0, -1])
        index = 1
        for i in range(length_of_s - 1):
            
            if not self.is_digit(s[i]) and self.is_digit(s[i+1]):
                value = meta_data[index - 1]
                x = value[0]
                y = value[1]
                end = i
                meta_data.append([ y+1, y + end-start+1, s[start:end+1] ])
                start = end
                index = index + 1
            elif self.is_digit(s[i]):
                value = meta_data[index - 1]
                x = value[0]
                y = value[1]
                frequency = int(s[i])
                meta_data.append([ y+1, y*frequency, frequency])
                index = index + 1
                start = i + 1
        
        i  = i + 1
        
        if self.is_digit(s[i]):
            value = meta_data[index - 1]
            x = value[0]
            y = value[1]
            frequency = int(s[i])
            meta_data.append([ y+1, y*frequency, frequency])
            index = index + 1
            start = i + 1
        else:
            value = meta_data[index - 1]
            y = value[1]
            end = i
            meta_data.append([ y+1, y + end-start+1, s[start:end+1] ])
            start = end
            index = index + 1
        # creating meta data ends here
        
        for i in range(len(meta_data)-1, 0, -1):
            # print(meta_data[i])
            value = meta_data[i]
            lower = value[0]
            upper = value[1]
            func = value[2]
            if k <= upper and k >= lower:
                if type(func) == type(1):
                    k = self.reduce_index(upper, lower, func, k)
                else:
                    result = func[k - lower]
                    break
        return result     
    
    def reduce_index(self, upper, lower, frequency, k):
        #return k-(upper - lower + 1)
        #print(f'{lower} {upper} {frequency} {k}')
        res = k % int(((upper  -lower +1)/(frequency-1)))
        if res == 0: 
            res = int(((upper  -lower +1)/(frequency-1)))
        return res

    def is_digit(self, ch):
        if ch >= '0' and ch <= '9':
            return True
        else:
            return False

if __name__ == '__main__':
    str = input()
    index = int(input())
    #print(len(str))
    obj = Solution()
    
    length = 53
    for i in range(1, 53):
        res = obj.decodeAtIndex(str, i)
        print(res, end='\t')
    print()
    for i in range(1, 53):
        print(i, end='\t')
    #res = obj.decodeAtIndex(str, 8)
    #print(res)