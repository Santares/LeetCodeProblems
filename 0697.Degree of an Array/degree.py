from typing import List


# def findShortestSubArray(self, nums: List[int]) -> int:
#     degree = {}
#     max_degree = 0
#     max_degree_nums = set()
#     for x in nums:
#         if x in degree:
#             degree[x] += 1
#         else:
#             degree[x] = 1
#         if degree[x] == max_degree:
#             max_degree_nums.add(x)
#         elif degree[x] > max_degree:
#             max_degree_nums.clear()
#             max_degree_nums.add(x)
#             max_degree = degree[x]
#
#     nums_record = {}
#     i = 0
#     for x in nums:
#         i += 1
#         if x in max_degree_nums:
#             if x in nums_record:
#                 if nums_record[x][0] == max_degree - 1:
#                     return i - nums_record[x][1] + 1
#                 else:
#                     nums_record[x][0] += 1
#             else:
#                 nums_record[x] = [1, i]
#
#     return len(nums) - i + 1



def findShortestSubArray2(self, nums: List[int]) -> int:
    degree = {}
    max_degree = 0
    max_degree_nums = set()
    for x in nums:
        if x in degree:
            degree[x] += 1
        else:
            degree[x] = 1
        if degree[x] == max_degree:
            max_degree_nums.add(x)
        elif degree[x] > max_degree:
            max_degree_nums.clear()
            max_degree_nums.add(x)
            max_degree = degree[x]

    nums_record = {}
    min_len = 50000
    i = 0
    for x in nums:
        i += 1
        if x in max_degree_nums:
            if x in nums_record:
                nums_record[x][1] = i
                if nums_record[x][2] == max_degree - 1:
                    length = nums_record[x][1] - nums_record[x][0] + 1
                    if length < min_len:
                        min_len = length
                else:
                    nums_record[x][2] += 1
            elif max_degree == 1:
                return 1
            else:
                nums_record[x] = [i, i, 1]

    return min_len


def findShortestSubArray2_2(self, nums: List[int]) -> int:
    degree = {}
    max_degree = 0
    i = 0
    for x in nums:
        i += 1
        if x in degree:
            degree[x][0] += 1
            degree[x][2] = i - degree[x][1] + 1
        else:
            degree[x] = [1, i, 0]
        max_degree = max(max_degree, degree[x][0])

    if max_degree == 1:
        return 1

    min_len = 50000
    for k, v in degree.items():
        if v[0] == max_degree:
            min_len = min(min_len, v[2])

    return min_len


if __name__ == '__main__':
    # test = [1, 2, 2, 3, 1]
    test = [1,2,2,3,1,4,2]
    # test = [1]
    # test = [2,1,1,2,1,3,3,3,1,3,1,3,2]
    # test = [1,2,2,1,2,1,1,1,1,2,2,2]
    res = findShortestSubArray2_2(0, test)
    print(res)


# online solution
def findShortestSubArray3(self, nums: List[int]) -> int:
    maxv = 0
    d = {}
    count = 1000000
    for i in nums:
        if i in d:
            d[i] += 1
            maxv = max(maxv, d[i])
        else:
            d[i] = 1

    if maxv <= 1:
        return 1

    for i, k in d.items():
        start = end = 0
        if k == maxv:
            for num in range(len(nums)):
                if nums[num] == i:
                    start = num
                    break
            for num in range(len(nums) - 1, -1, -1):
                if nums[num] == i:
                    end = num
                    break
        else:
            continue

        if count > (end - start + 1):
            count = end - start + 1

        print(count)
    return count

# online solution
def findShortestSubArray4(self, nums: List[int]) -> int:
    d = {}
    m, j, count = 1, [nums[0]], []
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            if d[i] > m:
                m = d[i]
                j = [i]
            elif d[i] == m:
                j.append(i)
    for i in j:
        count.append(len(nums) - nums[::-1].index(i) - nums.index(i))
    return min(count)