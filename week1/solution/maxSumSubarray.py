class Solution:
    '''
    input:
        nums: integer array
        
    output:
        result: integer that is the largest subarray sum
        
    edge cases:
        all nums positive - entire array sum
        all nums negative - largest number in array
        
    constraints:
        atleast 1 element in array
        array has positive or negative integers
        
    brute force idea:
        .....
    
    optimization:
        ....
        
        
    pseudocode:
        
        def maxArray(self, nums):
            max_sum = -INF
            current_sum = 0
            
            for num in nums:
                # choose between adding to current subarray OR starting NEW subarray
                
                if current_sum+num > num:
                    current_sum+= num
                else:
                    current_sum = num
                
                if current_sum > max_sum:
                    max_sum = current_sum
            
            return max_sum      
    
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            
            current_sum = current_sum+num if current_sum+num > num else num
                
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum
                