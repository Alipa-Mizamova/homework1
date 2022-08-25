def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, list, target):
        mid = len(list) // 2
        low = 0
        high = len(list) - 1

        while list[mid] != target and low <= high:
            if target > list[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            print("No target")
        else:
            print("ID =", mid)

