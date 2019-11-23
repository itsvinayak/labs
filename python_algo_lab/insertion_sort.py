def insertion_sort(array):

    for i in range(len(array)):
        cursor = array[i]
        pos = i

        while pos > 0 and array[pos - 1] > cursor:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[pos] = cursor

    return array


if __name__ == "__main__":
    print(insertion_sort([1, 3, 9, 2, 0, 3, 4, 8]))
