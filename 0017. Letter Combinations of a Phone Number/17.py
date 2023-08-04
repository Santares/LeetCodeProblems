from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        def helper(current, rest):
            if len(rest) == 0:
                return current
            next = rest[0]

            new = []
            for letter in dict[next]:
                for prev in current:
                    new.append(prev+letter)
            return helper(new, rest[1:])

        if len(digits) == 0:
            return []

        return helper(dict[digits[0]], digits[1:])

if __name__ == '__main__':
    test1 = '23'
    solution = Solution()
    print(solution.letterCombinations(test1))
