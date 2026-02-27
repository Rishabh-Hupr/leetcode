class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        '''
            https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
            Time: O(nlog(n))
            Space: O(1)
            
            NOTE: We need to calculate the weight of each number, which is the number of 1 bits in its binary representation.
            The way we calculate the weight is we do an AND op of the number with 1 to check if the least significant bit is 1, if it is we increment the weight and then we do an XOR op to remove that bit from the number(because XOR sets same bits to 0 and diff bits to 1). We repeat this process until the number becomes 0.
            We can do this by using a mask to check each bit of the number and counting how many times we find a 1 bit.
            After calculating the weight, we can sort the array based on the weight and then by the number itself if there are ties in weight.
        '''
        def find_weight(num):
            mask = 1
            weight = 0
            
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask
                
                mask <<= 1
            
            return weight
        
        arr.sort(key = lambda num: (find_weight(num), num))
        return arr