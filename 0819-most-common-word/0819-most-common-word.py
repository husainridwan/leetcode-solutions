class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.": 
            paragraph = paragraph.replace(c, " ")
        d, common, count = {},"",0
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in d:
                d[word] += 1
            else:
                d[word] = 1
            if d[word] > count:
                count = d[word]
                common = word
        return common
    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                