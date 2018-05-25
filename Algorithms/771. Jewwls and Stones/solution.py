class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(0, len(J)):
            for j in range(0, len(S)):
                if J[i] == S[j]:
                    count +=1
        return count