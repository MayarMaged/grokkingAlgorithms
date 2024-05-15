def binary_search(sorted_arr, item):
    """
    :param sorted_arr:
    :param item:
    :return: index of item if found, if not found return -1
    """
    arr_length = len(sorted_arr)
    low = 0
    high = arr_length - 1
    middle = (arr_length -1) // 2
    if item == sorted_arr[middle]:
        return middle
    else:
        while low < high:
            if item > sorted_arr[middle]:
                low = middle + 1
            elif item < sorted_arr[middle]:
                high = middle - 1
            elif item == sorted_arr[middle]:
                return middle
            middle = ((high - low) //2 ) + low
        if low == high:
            if item == sorted_arr[low]:
                return low
        return -1



def binary_search_recursive(low: int, high: int, sorted_arr, item) -> int:
    if low == high or low > high:
        if item == sorted_arr[low]:
            return low
        return -1
    middle = ((high - low) // 2 ) + low
    if item == sorted_arr[middle]:
        return middle
    elif item > sorted_arr[middle]:
        return binary_search_recursive(middle +1, high, sorted_arr, item)
    elif item < sorted_arr[middle]:
        # checks
        return binary_search_recursive(low, middle - 1, sorted_arr, item)


# print(binary_search([1,4,6,7,8,10,14,70,80,88,89,90, 100, 200, 201, 204, 300, 350], 90))