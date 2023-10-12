# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 0
        right = mountain_arr.length()
        top = 0

        while left <= right:
            mid = (left + right) // 2

            l = mountain_arr.get(mid - 1) if mid - 1 >= 0 else -1
            m = mountain_arr.get(mid)
            r = mountain_arr.get(mid + 1) if mid + 1 < mountain_arr.length() else -1

            if l < m and r < m:
                top = mid
                break

            if l < m < r:
                left = mid + 1
            elif l > m > r:
                right = mid - 1

        left = 0
        right = top

        while left <= right:
            mid = (left + right) // 2
            m = mountain_arr.get(mid)

            if m == target:
                return mid

            if m < target:
                left = mid + 1
            else:
                right = mid - 1

        left = top
        right = mountain_arr.length() - 1

        while left <= right:
            mid = (left + right) // 2
            m = mountain_arr.get(mid)

            if m == target:
                return mid

            if m > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
