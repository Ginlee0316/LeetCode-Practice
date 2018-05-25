class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        
        for i,matrix in enumerate(A):
            tmp = []
            for binary in matrix:
                if binary == 1 :
                    binary = 0
                else:
                    binary = 1
                tmp.append(binary)
            tmp.reverse()
            result.append(tmp)
        return result
                    