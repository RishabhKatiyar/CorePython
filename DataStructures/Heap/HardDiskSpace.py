def GetMaxInMin(x, space):
    import heapq
    # heapq.heapify(space)
    # print(space)
    min_list = []    
    minHeap = []
    
    for i in range(x):
        minHeap.append(space[i])
    heapq.heapify(minHeap)
    min_list.append(minHeap[0])
    #print(min_list)
    for i in range(x, len(space)):
        remove = space[i-x]
        add = space[i]
        minHeap.remove(remove)
        minHeap.append(add)
        heapq.heapify(minHeap)
        min_list.append(minHeap[0])
    # print(min_list)
    
    max = None
    for min in min_list:
        if max == None:
            max = min
        elif max < min:
            max = min
    
    return max


if __name__ == "__main__":
    list = [1,5,1,6,7,8,2,3]
    x = 5
    result = GetMaxInMin(x, list)
    print(result)