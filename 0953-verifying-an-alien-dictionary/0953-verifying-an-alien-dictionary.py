class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {}
        for idx, val in enumerate(order):
            hashMap[val] = idx
        
        for i in range(len(words) - 1):
            curr, after = words[i], words[i+1]
            l = r = 0
            check = True
            while l < len(curr) and r < len(after):
                if curr[l] == after[r]:
                    l += 1
                    r += 1
                else:
                    if hashMap[curr[l]] < hashMap[after[r]]:
                        check = False
                        break 
                    else:
                        return False
            if check:
                if len(curr) > len(after):
                    return False
        return True