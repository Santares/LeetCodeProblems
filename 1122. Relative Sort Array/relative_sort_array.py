from typing import *

# 1.Traverse array 1 and build a map with key = number in array 1, value = times it occurs in array 1
# 2.Create a new empty array 3
# 3.Traverse array 2, append the number into array 3 as many times as the value in the map, delete the pair in map
# 4.Traverse the rest of the map, add the number into another array array 4. Sort the array 4 at last
# 5.Join the array 3 and 4
# 6.Return the array 3
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    dic = {}
    for x in arr1:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

    output = []

    for x in arr2:
        for i in range(0, dic[x]):
            output.append(x)
        dic.pop(x)

    temp = []
    for x in dic:
        for i in range(0, dic[x]):
            temp.append(x)

    return output + sorted(temp)


# faster
def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
    dic = {}
    output = []
    rest = []
    arr2_set = set(arr2)
    for x in arr1:
        if x in arr2_set:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
        else:
            rest += [x]  # change point

    for x in arr2:
        output += [x] * dic[x]  # change point
    return output + sorted(rest)

if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
    arr2 = [2,42,38,0,43,21]
    res = [2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]
    output = relativeSortArray(0, arr1, arr2)
    print(output)
    print(res)
