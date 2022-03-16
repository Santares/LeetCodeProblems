from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        l = len(pushed)

        while i < l or j < l:
            if i == l and j < l:
                if popped[j] != stack[-1]:
                    return False
                else:
                    j += 1
                    stack.pop()
            elif i < l and j == l:
                return False
            else:
                x = pushed[i]
                y = popped[j]
                if x == y:
                    i += 1
                    j += 1
                elif len(stack) == 0:
                    stack.append(x)
                    i += 1
                elif y == stack[-1]:
                    j += 1
                    stack.pop()
                else:
                    stack.append(x)
                    i += 1

        return True

    # online solution
    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        i, X = 0, []
        for x in pushed:
            while X and X[-1] == popped[i]:
                X.pop()
                i += 1

            X.append(x)

        while X and X[-1] == popped[i]:
            X.pop()
            i += 1

        return not X

    # online solution
    def validateStackSequences3(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return i == len(popped)

if __name__ == '__main__':
    solution = Solution()
    test1 = [1,2,3,4,5]
    test2 = [4,5,3,2,1]
    test1 = [1,2,3,4,5]
    test2 = [4,3,5,1,2]
    print(solution.validateStackSequences(test1, test2))