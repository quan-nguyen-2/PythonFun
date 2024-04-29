def mode(nums):
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_count_num = max(count_dict, key=count_dict.get)
    return max_count_num
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
