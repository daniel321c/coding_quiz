class Solution:
    def sequentialString(self, s):
        startIndex = 0
        start = s[0]

        result = []
        for i in range(1, len(s)):
            if(not (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i])-ord(s[i-1])==-25)):
                result.append(s[startIndex:i])
                startIndex = i
                start = s[i]
        result.append(s[startIndex:])
        return result

    def findSubstringInWraproundString(self, p: str) -> int:
        
        if(p == ''):
            return 0
        listOfSubstrings = self.sequentialString(p)
        
        arr = [0]*26
        
        for s in listOfSubstrings:
            for i in range(len(s)):
                arr[ord(s[i])-ord('a')] = max(arr[ord(s[i])-ord('a')], len(s)-i)
        
        result = sum(arr)
        
        return result
