def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)

        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)


if __name__ == "__main__":
    array = [2, 4, 1, 4, 2, 0, 3, 3, 7]
    length = len(array) - 1

    quick_sort(array, 0, length)

    print(array)
