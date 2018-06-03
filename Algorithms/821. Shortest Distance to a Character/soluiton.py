class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        lis = []
        maxL = 9999
        for i,char in enumerate(S):
            if char == C :
                lis.append(i)
                
        for i in range(len(S)):
            tmp = maxL
            for j in lis :
                tmp = min(abs(i - j),tmp)
            result.append(tmp)
            
        return result