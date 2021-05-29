"""
Generate all permutations of a string

References:
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
https://www.youtube.com/watch?v=GuTPwotSdYw
"""

def permute(my_string, left_ix, right_ix, permutations): 
    if left_ix == right_ix:
        permutations.append("".join(my_string))
    else:
        for i in range(left_ix, right_ix + 1):
            my_string[left_ix], my_string[i] = my_string[i], my_string[left_ix]
            permute(my_string, left_ix + 1, right_ix, permutations)
            my_string[left_ix], my_string[i] = my_string[i], my_string[left_ix]
 
my_string = "".join((str(i) for i in range(4)))
n = len(my_string)
my_string = list(my_string)
permutations = []
permute(my_string, 0, n-1, permutations)
print(permutations)
