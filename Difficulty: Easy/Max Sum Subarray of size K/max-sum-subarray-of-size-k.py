class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        max_sum= sum(arr[:k])
        sum1 = max_sum
        for i in range(len(arr)-k):
            sum1=sum1 + arr[k+i]-arr[i]
            max_sum = max(max_sum,sum1)
            
        return max_sum