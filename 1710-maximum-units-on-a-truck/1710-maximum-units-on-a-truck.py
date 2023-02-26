class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        totalUnits = 0
        
        for boxes, boxUnits in boxTypes:
            numBoxes = min(truckSize, boxes)
            totalUnits += numBoxes * boxUnits
            truckSize -= numBoxes
            # if truckSize == 0:
            #     return totalUnits
        return totalUnits