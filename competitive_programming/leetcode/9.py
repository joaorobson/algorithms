import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = True
        if x < 0:
            res = False
        elif x == 0:
            res = True
        else:
            n_digits = int(math.log10(x) + 1)

            for i in range(n_digits//2):
                a = x%(10**(n_digits - i))//(10**(n_digits - i - 1))
                b = x%(10**(i + 1))//(10**(i))

                if a != b:
                    res = False
                    break

        return res

s = Solution()

x = int(input())

print(s.isPalindrome(x))
