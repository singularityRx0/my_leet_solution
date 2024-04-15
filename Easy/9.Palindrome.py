# Given an integer x, return true if x is a palindrome, and false otherwise.

# Constraints:

#     -2^31 <= x <= 2^31 - 1

 
# Follow up: Could you solve it without converting the integer to a string?

"""
        Exp:
            121
            x % 121 = 12.1 the % operator returns the 1
            half = (0) + (1) = 1
            x becomes 12
            since x > half continues

            half = (1*10) + 2 = 12
            x becomes 1
            since x < half stop loop

            half // 10 = 1
            so, x = 1 same as half = 1. Therefore ture
        """



class Palindrome:
    def isPalindrome(self, x: int) -> bool:

        nums = x

        if x < 0 or (x !=0 and x % 10 == 0):
            reversed_str = str(x)[::-1]
            reversed_num = reversed_str
            print()
            print('Input: x = {}'.format(x))
            print('Outpute: {}'.format(False))
            print('Explaination: From left to right, it reads {}. From right to left it becomes {}.'.format(x,reversed_num))
            return False
            
        half = 0
           
        while x > half:
            half = (half * 10) + (x % 10)
            x //= 10


        if x == half or x == half // 10:
            print()
            print('Input: x = {}'.format(nums))
            print('Outpute: {}'.format(True))
            print('Explaination: {} reads as {} from left to right and form right to left.'.format(nums,nums))
            return x == half or x == half // 10
        else:
            reversed_str = str(nums)[::-1]
            reversed_num = reversed_str
            print()
            print('Input: x = {}'.format(nums))
            print('Outpute: {}'.format(False))
            print('Explaination: From left to right, it reads {}. From right to left it becomes {}.'.format(nums,reversed_num))
            return x == half or x == half // 10



if __name__ == "__main__":
    solution = Palindrome()

    result = solution.isPalindrome(010)

    print()
    print('Actual output: {}'.format(result))














# class Palindrome:
#     def isPalindrome(self, x: int) -> bool:
#         number = x
#         reversed_digits = []
#         digits = []

#         if number >= -231 and number <= 230:
#             while number > 0:
#                 num = number % 10
#                 reversed_digits.append(num)
#                 digits.append(num)
#                 number //= 10

#             digits.reverse()
#             print(digits)
#             if digits == digits[::-1]:
#                 print('Input: x = {}'.format(x))
#                 print('Outpute: {}'.format(True))
#                 print('Explaination: {} reads as {} from left to right and form right to left.'.format(x,x))
#             else:
#                 print('Input: x = {}'.format(x))
#                 print('Outpute: {}'.format(False))
#                 print('Explaination: From left to right, it reads {}. From right to left it becomes {}'.format(x,int(''.join(map(str,reversed_digits)))))
#         else:
#             print('Value of x exceeded the constraints')