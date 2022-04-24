"""
Generate all combinations of 2*n matched parenthesis

Example:

n = 2
result = (()), ()()

References:
https://www.youtube.com/watch?v=sz1qaKt0KGQ
https://www.youtube.com/watch?v=sz1qaKt0KGQ
"""


def generate_matched_parenthesis_combinations(l, s, n_left, n_right):
    if n_left == 0 and n_right == 0:
        l.append(s)
        return
        
    if n_left == n_right:
        generate_matched_parenthesis_combinations(l, s + "(", n_left - 1, n_right)
    elif n_left < n_right:
        if n_left:
            generate_matched_parenthesis_combinations(l, s + "(", n_left - 1, n_right)
        if n_right:
            generate_matched_parenthesis_combinations(l, s + ")", n_left, n_right - 1)

num_parenthesis = int(input())

combinations = []
generate_matched_parenthesis_combinations(combinations, "", num_parenthesis, num_parenthesis)
print(combinations)
