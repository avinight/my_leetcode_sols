from typing import List


def find(nums: List[int], first: int, last: int, target: int) -> int:
    if nums[first] == target:
        return first
    elif nums[last] == target:
        return last
    elif first >= last:
        return -1
    else:
        mid = (first + last) // 2
        if target <= nums[mid]:
            return find(nums, first, mid, target)
        else:
            return find(nums, mid + 1, last, target)


def search(nums: List[int], target: int) -> int:
    """Return the index of <t> in <lst>, or -1 if it does not occur.

    Preconditions:
    - L is sorted.
      Specifically, lst[0] <= lst[1] ... <= lst[n-1], where n is len(lst).
    - t can be compared to the elements of lst.
    >>> search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5)
    1
    >>> search([2, 4, 7, 8, 11], 11)
    4
    >>> search([2, 4, 7, 8, 11], 5)
    -1
    """
    first = 0
    last = len(nums) - 1
    return find(nums, first, last, target)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
