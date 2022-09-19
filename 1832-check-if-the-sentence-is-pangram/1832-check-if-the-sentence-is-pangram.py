class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #return len(set(sentence)) == 26
        
        check = {}
        for i in sentence:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
        if len(check) == 26:
            return True