"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""

# Constraints:

#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class RomantoInt:
    def romantoint(self, s: str ) -> int:
        array = list(s)
        Roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        curr = 0
        prev = 0

        # print(Roman_map[array[0]])

        print(array[::-1])
        

        for i in range(-1, -len(array) - 1, -1):
            actual_index = abs(i)

            curr = Roman_map[array[i]]
            print()
            if i == -1:
                total = curr
                prev = curr
                print('|Step {}|    condition 1 curr: {}     prev: {}    total: {}'.format(actual_index,curr, prev, total))
            elif i != -1 and curr < prev:
                total -= curr
                prev = curr
                print('|Step {}|    condition 2 curr: {}     prev: {}    total: {}'.format(actual_index,curr, prev, total))
            else:
                total += curr
                prev = curr
                print('|Step {}|    condition 3 curr: {}     prev: {}    total: {}'.format(actual_index,curr, prev, total))

        print()
        
        return total

if __name__ == "__main__":
    solution = RomantoInt()

    result = solution.romantoint("LVIII")

    print(result)
