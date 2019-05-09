class Solution(object):
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        nums = even + odd
        return nums
