'''
def solution(nums, N):
    N = str(N)
    length = len(N)
    nums.sort(reverse=True)

    def helper(i, cur):
        if i == length - 1:
            for x in nums:
                if x < int(N[i]):
                    cur.append(str(x))
                    return int(''.join(cur))
            return -1
        else:
            for x in nums:
                if x == int(N[i]):
                    cur.append(str(x))
                    res = helper(i + 1, cur)
                    if res != -1:
                        return res
                    cur.pop()
                elif x < int(N[i]):
                    cur.append(str(x))
                    cur += str(nums[0]) * (length - i - 1)
                    return int(''.join(cur))

        return -1

    res = helper(0, [])
    if res != -1:
        return res

    if length > 1:
        return int(str(nums[0]) * (length - 1))
    else:
        return -1
'''
import bisect


def solution(nums, N):
    nums.sort()
    N = str(N)
    k = len(N)
    numsSet = set(nums)
    for i in range(k - 1, -1, -1):
        isValid = True
        for j in range(i):
            if int(N[j]) not in numsSet:
                isValid = False
                break
        if isValid:
            # for x in nums[::-1]:
            #     if x < int(N[i]):
            #         return int(N[:i] + str(x) + str(nums[-1]) * (k-i-1))
            j = bisect.bisect_left(nums, int(N[i]))
            if j > 0:
                return int(N[:i] + str(nums[j-1]) + str(nums[-1]) * (k - i - 1))
    return int(str(nums[-1]) * (k - 1))


if __name__ == '__main__':
    test1 = [1, 2, 9, 4]
    test2 = 2499  # 2494
    test2 = 2533  # 2499
    test1 = [1, 2, 5, 4]
    test2 = 2543  # 2542
    test1 = [1, 2, 5, 4]
    test2 = 2541  # 2525
    test1 = [1, 2, 9, 4]
    test2 = 2111  # 1999
    test1 = [5, 9]
    test2 = 5555  # 999
    # print(solution(test1, test2))
    print(solution([1, 2, 9, 4], 2499) == 2494)
    print(solution([1, 2, 9, 4], 2533) == 2499)
    print(solution([1, 2, 5, 4], 2543) == 2542)
    print(solution([1, 2, 5, 4], 2541) == 2525)
    print(solution([1, 2, 9, 4], 2111) == 1999)
    print(solution([5, 9], 5555) == 999)
    print(solution([2], 1111) == 222)
    print(solution([1,2], 12121) == 12112)


'''
O(n log n) + O(k) + O(n) + O(k * (k + log n))
O(n log n) + O(k) + O(n * k)
'''
