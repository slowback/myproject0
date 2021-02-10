x = 1534236469


class Solution:
    def reverse(self, x: int) -> int:

        if x > 0:
            x = str(x)
            x = int(x[::-1])
            check = ( (x < 2 ** 31) and (x > (-2 ** 31) - 1) ) or 0
            if check:
                return x
            return check

        elif x < 0:
            x = str(x)
            x = int('-' + x[-1:0:-1])
            check = ((x < 2 ** 31) and (x > (-2 ** 31) - 1)) or 0
            if check:
                return x
            return check

        else:
            return 0


s = Solution()
print(s.reverse(x))
