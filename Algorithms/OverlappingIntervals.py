def merge_intervals(ar_list):
    #print(inp)
    result = [[None]*2 for _ in range(1)]
    #print(result)
    i = 0
    count = 0
    length1 = len(ar_list) 
    while i  < (length1):
        # print(ar_list[i])
        j = i+1
        result[count][0] = ar_list[i][0]
        while True:
            if j < len(ar_list):
                prev = ar_list[i][1]
                new = ar_list[j][0]
                if prev >= new:       
                    pass
                else:
                    break
            else:
                break
            j += 1
        result[count][1] = ar_list[j-1][1]
        count += 1
        result.append([None, None])
        i = j
    length = len(result)
    return result[:length-1]
# 1 3 4 5 6 7 9 9  3 3
if __name__ == "__main__":
    inp = [[1,3],[2,6],[8,10],[15,18]]
    #inp = [[1,4],[5,6], [7,8], [9,20]]
    print(merge_intervals(inp))
    