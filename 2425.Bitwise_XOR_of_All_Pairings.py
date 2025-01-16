class Solution(object):
    def xorAllNums(self, nums1, nums2):
        result = 0  
        for num1 in nums1:  
            for num2 in nums2:  
                result ^= (num1 ^ num2)  
        return result  
