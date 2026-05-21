#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k):
        # code here
        q=deque()
        ans=[]
        for i in range(0,len(arr)):
            if arr[i]<0:
                q.append(arr[i])
            if i>=k-1:
                if q:
                    ans.append(q[0])
                else:
                    ans.append(0)
                if q and arr[i-k+1]==q[0]:
                    q.popleft()
        return ans