# The guess API is already defined for you.
# def guess(num):

class Solution:
    def guessNumber(self, n):

        low = 1
        high = n

        while low <= high:

            mid = (low + high) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == 1:
                low = mid + 1

            else:
                high = mid - 1