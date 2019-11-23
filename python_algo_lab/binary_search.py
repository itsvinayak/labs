def binary_search(array, left, right, item):
    if left > right:
        return -1
    mid = (left + right) // 2

    if item < array[mid]:
        return binary_search(array, left, mid - 1, item)
    elif item > array[mid]:
        return binary_search(array, mid + 1, right, item)
    else:
        return mid


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 8
    print(binary_search(array, 0, len(array), 3))
