class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first = second = -1
        
        for x in arr:
            if x > first:
                second = first
                first = x
            elif x > second and x != first:
                second = x
                
        return second