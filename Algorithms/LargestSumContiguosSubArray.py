from sys import maxsize

def maxSubArraySum(a):
    max_so_far = a[0]
    max_ending_here = 0
    size = len(a)
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

#a = [-13,-3,-25,-20,-3,-16,-23,-12,-5,-22,-15,-4,-7] 
a = [-2, -3, 4, -1, -2, 1, 5, -3] 

print(maxSubArraySum(a))