class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes_sorted = sorted(boxTypes, key=lambda x: x[1],reverse=True ) # True descending order sort
        truckSizeLimitMax = truckSize
        maxUnits = 0
        for item in boxTypes_sorted:
            if truckSizeLimitMax == 0:
                break
            if item[0] <= truckSizeLimitMax:
                maxUnits = maxUnits + item[0]*item[1]
                truckSizeLimitMax = truckSizeLimitMax - item[0]
            else:
                maxUnits = maxUnits + truckSizeLimitMax*item[1]
                truckSizeLimitMax = 0
            print(item,' truckSize: ',truckSize,' remaining space: ',truckSizeLimitMax,' maxUnits: ',maxUnits)
        return maxUnits
                

        




# time complexity: O(Length of boxTypes) and space complexity: O(Length of boxTypes)
