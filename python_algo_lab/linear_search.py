def linear_search(array, left, right, item):
    if left == right:
        return -1
    if array[left] == item:
        return left + 1
    return linear_search(array, left + 1, right, item)


if __name__ == "__main__":

    array = [1, 3, 9, 22, 5, 0, 3, 3, 4, 90]
    item = 22
    right = len(array)
    print(linear_search(array, 0, right, item))
