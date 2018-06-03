class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ~num + 2**num.bit_length()