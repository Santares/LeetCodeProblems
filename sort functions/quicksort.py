import random


def quicksort(nums, left, right):
    if left >= right:
        return

    pivot = nums[left]
    last = left + 1

    for i in range(left + 1, right + 1):
        if nums[i] <= pivot:
            nums[last], nums[i] = nums[i], nums[last]
            last += 1

    last -= 1
    nums[last], nums[left] = nums[left], nums[last]
    quicksort(nums, left, last - 1)
    quicksort(nums, last + 1, right)

    return


def quicksort2(nums, left, right):
    if left >= right:
        return

    pivot = nums[left]

    i, j = left, right

    while i < j:
        while nums[i] <= pivot and i < j:
            i += 1
        while nums[j] > pivot and j > i:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    last = i - 1
    nums[last], nums[left] = nums[left], nums[last]
    quicksort(nums, left, last - 1)
    quicksort(nums, last + 1, right)

    return


if __name__ == '__main__':
    for _ in range(100):
        nums = [x for x in range(1000)]
        random.shuffle(nums)
        snums = sorted(nums)
        quicksort2(nums, 0, len(nums) - 1)

        if snums != nums:
            print(False)
            exit(0)

    print(True)
