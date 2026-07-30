
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        def findLast():
            l, r = 0, len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return ans

        first = findFirst()

        if first == -1:
            return [-1, -1]

        last = findLast()

        return [first, last]