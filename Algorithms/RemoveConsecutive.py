def remove_consecutive(ar, k):
    i = 0
    min_amplitude = None

    for i in range(len(ar)-k+1):
        j = i
        m = 0
        min = None
        max = None
        
        for m in range(j):
            #print(f'{ar[m]}', end = '\t')
            if min == None:
                min = ar[m]
            elif min > ar[m]:
                min = ar[m]
            if max == None:
                max = ar[m]
            elif max < ar[m]:
                max = ar[m] 

        j = j + k

        for m in range(j, len(ar)):
            #print(f'{ar[n]}', end = '\t')
            if min == None:
                min = ar[m]
            elif min > ar[m]:
                min = ar[m]
            if max == None:
                max = ar[m]
            elif max < ar[m]:
                max = ar[m] 
        
        if min_amplitude == None:
            min_amplitude = max - min
        elif min_amplitude > max - min:
            min_amplitude = max - min 

    return min_amplitude

if __name__ == "__main__":
    ar = [3,5,1,3,9,8]
    k = 4
    print(remove_consecutive(ar, k))