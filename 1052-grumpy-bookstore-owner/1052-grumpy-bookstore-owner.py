class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """total = 0
        for i in range(len(grumpy)-minutes+1):
            if grumpy[i] == 0:
                total += customers[i]
                total = total + sum(customers[:len(customers)-minutes])
        return total"""
        
        # a sliding window approach
        currsum = 0
        # first store the sum as if the owner has no super power
        for i in range(len(grumpy)):
            if not grumpy[i]:
                currsum += customers[i]
        
        # now assuming he has the power, take the first window and add to the previous sum
        for i in range(minutes):
            if grumpy[i]:
                currsum += customers[i]
        
        maxsum = currsum
        # Now the sliding window starts
        # i and j are the two opposite ends of the window
        i = 0
        j = minutes
        while j < len(customers):
            if grumpy[j]:
                currsum += customers[j]
            if grumpy[i]:
                currsum -= customers[i]
			# we subtract above as the window has already passed over that customer
            if currsum > maxsum:
                maxsum = currsum
            i += 1
            j += 1
        return maxsum