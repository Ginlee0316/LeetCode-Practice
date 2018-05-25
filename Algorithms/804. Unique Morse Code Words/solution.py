class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MorseCode_a2z =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        
        for word in words:
            tmp = ""
            for char in word:
                tmp += MorseCode_a2z[ord(char)-ord('a')]
            result.add(tmp)
        return len(result)