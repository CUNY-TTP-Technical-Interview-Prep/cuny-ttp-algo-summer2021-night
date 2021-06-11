from typing import List
class Solution:
  def countGoodTriplets2(self, arr: List[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    count = 0
    for i in range(n-2):
      for j in range(i+1, n-1):
        if abs(arr[i] - arr[j]) > a: continue
        count += sum(abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c for k in range(j+1, n))
    return count
    
  def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n-2):
      for k in range(i+2, n):
        if abs(arr[i] - arr[k]) > c: continue
        count += sum(abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b for j in range(i+1, k))
    return count

arr = [1,1,2,2,3]; a = 0; b = 0; c = 1
arr = [7,3,7,3,12,1,12,2,3]
a = 5
b = 8
c = 1
arr = [3,0,1,1,9,7]; a = 7; b = 2; c = 3

Sol = Solution()
ans = Sol.countGoodTriplets(arr, a,b,c)
print(ans)