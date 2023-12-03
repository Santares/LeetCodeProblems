def find_shortest_subarray(A, C):
    positions = {element: [] for element in C}
    result = []
    max_index = -1
    min_length = float('inf')

    for i, num in enumerate(A):
        if num in positions:
            positions[num].append(i)

    for num in C:
        if not positions[num]:
            return []

        last_position = positions[num][-1]

        if last_position > max_index:
            max_index = last_position

        if num == C[-1] and max_index != -1:
            current_length = max_index - positions[C[0]][0] + 1
            if current_length < min_length:
                min_length = current_length
                result = A[positions[C[0]][0]: max_index + 1]

    return result


if __name__ == '__main__':
    # 示例
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 3, 10]
    C = [3, 7, 10]
    # A = [1, 2, 3, 4, 5, 6, 7, 8]
    # C = [3, 4, 5]

result = find_shortest_subarray(A, C)
print(result)  # 输出 [3, 4, 5]
