input_string = "abcd"
purmutations_set = set()

def list_to_str(string):
    permutation = ''
    for s in string:
        permutation = permutation + s
    return permutation


def permute(j, input_string, length):
    for i in range(j, length):
        string = list(input_string)
        string[j], string[i] = input_string[i], input_string[j]
        purmutations_set.add(list_to_str(string))
        permute(j+1, list_to_str(string), length)

permute(0, input_string, len(input_string))

import math
print(math.factorial(len(input_string)))

permutations_list = []
for permutation in purmutations_set:
    permutations_list.append(permutation)

permutations_list.sort()

for i in range(len(permutations_list)):
    print(f'{i+1} {permutations_list[i]}')
