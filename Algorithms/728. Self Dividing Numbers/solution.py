class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        result = list()
        
        for i in range(left, right + 1) :
            tmp = i
            isPass = 1
            while tmp != 0 :
                if tmp % 10 == 0 :
                    isPass = 0
                    break
                if i % (tmp % 10) != 0:
                    isPass = 0
                    break
                tmp = tmp // 10
            if isPass == 1 :
                result.append(i)
        return result       