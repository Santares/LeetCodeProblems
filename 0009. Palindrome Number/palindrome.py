class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        return s1 == s1[::-1]

    # online solution, without converting to string, slow
    def isPalindrome2(self, x: int) -> bool:
        divisor = 1
        while (x / divisor >= 10):
            divisor *= 10

        while (x != 0):

            leading = x // divisor
            trailing = x % 10

            # If first and last digit
            # not same return false
            if (leading != trailing):
                return False

            # Removing the leading and
            # trailing digit from number
            x = (x % divisor)//10

            # Reducing divisor by a factor
            # of 2 as 2 digits are dropped
            divisor = divisor/100

        return True