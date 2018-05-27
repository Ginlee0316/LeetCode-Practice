class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
             
        result = 0
        x2bin = bin(x)[2:]
        y2bin = bin(y)[2:]
        
        binx = list(x2bin)
        biny = list(y2bin)
        
        if len(binx) >= len(biny):
            length = len(binx)
            for i in range (length - len(biny)) :
                biny.insert(0,'0')
        else:
            length = len(biny)
            for i in range (length - len(binx)) :
                binx.insert(0,'0')
        
        for i in range(length) :
            if binx[i] != biny [i] :
                result +=1
        return result