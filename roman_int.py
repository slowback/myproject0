from functools import reduce


class Solution:
    def roman_int(self, s):
        roman_n = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Solution 1
        # i = 0
        # result = 0
        # while i < len(s):
        #     if i == len(s) - 1:
        #         result += roman_n[s[i]]
        #
        #     elif roman_n[s[i]] < roman_n[s[i + 1]]:
        #         result -= (roman_n[s[i]])
        #
        #     else:
        #         result += roman_n[s[i]]
        #     i += 1
        # return result

        # Solution 2
        return reduce(lambda s, c: s + roman_n[c]
        if s < roman_n[c] << 2 else s - roman_n[c], reversed(s), 0)


if __name__ == '__main__':
    s = "MCMXCIV"
    so = Solution()
    print(so.roman_int(s))

    # roman_n = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000
    # }
    # for k, v in roman_n.items():
    #     c = v << 2
    #     d = v >> 2
    #     print("{},{}: left shift 2 = ({})".format(k, v, c))
    #     # print("{},{}: right shift 2 = ({})".format(k, v, d))
    #     print()
    # print(list(reversed(s)))
