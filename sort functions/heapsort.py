import random

def heapsort(nums):
    res = []
    heap = []
    for x in nums:
        heappush(heap, x)

    while heap:
        res.append(heappop(heap))

    return res


def heapsort2(nums):
    heap = [x for x in nums]
    res = []
    heapify(heap)

    while heap:
        res.append(heappop(heap))
    return res


def getLeft(heap, i):
    j = i*2 + 1
    if j >= len(heap):
        return -1

    return j


def getRight(heap, i):
    j = i * 2 + 2
    if j >= len(heap):
        return -1

    return j


def getParent(heap, i):
    if i == 0:
        return -1

    j = i//2
    if i % 2 == 0:
        j-=1

    return j


def heapdown(heap, i):
    if i < len(heap)-1:
        left = getLeft(heap, i)
        right = getRight(heap, i)
        if left == right == -1:
            return
        elif left != -1 and right == -1:
            if heap[left] < heap[i]:
                heap[i], heap[left] = heap[left], heap[i]
                heapdown(heap, left)
        elif right != -1 and left == -1:
            if heap[right] < heap[i]:
                heap[i], heap[right] = heap[right], heap[i]
                heapdown(heap, right)
        else:
            if heap[left] < heap[right] and heap[left] < heap[i]:
                heap[i], heap[left] = heap[left], heap[i]
                heapdown(heap, left)
            elif heap[right] < heap[left] and heap[right] < heap[i]:
                heap[i], heap[right] = heap[right], heap[i]
                heapdown(heap, right)

    return


def heapup(heap, i):
    j = getParent(heap, i)
    if j == -1:
        return
    else:
        if heap[j] > heap[i]:
            heap[i], heap[j] = heap[j], heap[i]
            heapup(heap, j)

    return


def heappush(heap, x):
    heap.append(x)
    heapup(heap, len(heap)-1)
    return


def heappop(heap):
    if heap:
        x = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        heapdown(heap, 0)
        return x
    return None


def heapify(heap):
    def helper(heap, i):
        left = getLeft(heap,i)
        right = getRight(heap, i)
        if left != -1 and heap[left] < heap[i]:
            heap[i], heap[left] = heap[left], heap[i]
            helper(heap, left)
        if right != -1 and heap[right] < heap[i]:
            heap[i], heap[right] = heap[right], heap[i]
            helper(heap, right)

    for i in range(len(heap)//2 -1, -1, -1):
        helper(heap, i)

    return


if __name__ == '__main__':
    for _ in range(100):
        nums = [x for x in range(1000)]
        random.shuffle(nums)
        snums = sorted(nums)
        hnums = heapsort2(nums)

        if snums != hnums:
            print(False)
            print(nums)
            exit(0)

    print(True)

    # testheap = []
    # nums = [x for x in range(10)]
    # random.shuffle(nums)
    # nums = [5, 0, 7, 8, 9, 4, 6, 3, 2, 1]
    # for x in nums:
    #     heappush(testheap, x)
    # print(testheap)
    #
    # # testheap = [0, 1, 4, 3, 2, 7, 6, 8, 5, 9]
    # # testheap = [4,5,6,8,9,7]
    # while testheap:
    #     print(heappop(testheap))

    # nums = [x for x in range(7)]
    # random.shuffle(nums)
    # heapify(nums)
    # print(nums)