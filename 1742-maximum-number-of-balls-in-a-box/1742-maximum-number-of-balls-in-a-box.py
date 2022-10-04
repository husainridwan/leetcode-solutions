class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        check = {}
        for i in range(lowLimit,highLimit+1):
            boxNum = self.digitSum(i)
            check[boxNum] = check.get(boxNum,0) + 1
            
        maxNum = 0
        for j in check:
            if check[j] > maxNum:
                maxNum = check[j]
        return maxNum
    
    def digitSum(self,n):
        total = 0
        while n > 0:
            digit = n % 10
            total += digit
            n //= 10
        return total
    