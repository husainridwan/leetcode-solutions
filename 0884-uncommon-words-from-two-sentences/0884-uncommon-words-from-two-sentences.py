class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sentences = s1.split(" ") + s2.split(" ")
        common = {}
        for word in sentences:
            if word in common:
                common[word] += 1
            else:
                common[word] = 1
                
        uncommon = []
        for word in common:
            if common[word] == 1:
                uncommon.append(word)
        return uncommon            
        