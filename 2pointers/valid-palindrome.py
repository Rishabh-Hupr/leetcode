class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            https://leetcode.com/problems/valid-palindrome/description/
            Time: O(n)
            Space: O(1)
            NOTE: I did the whole setup here, without using inbuilt libraries
        '''
        # def valid(char):
        #     asci = ord(char)
        #     if 97 <= asci <= (97+25):
        #         asci -= 32
        #     if 65 <= asci <= (65+25) or 48 <= asci <= 57:
        #         return (True, asci)
        #     return (False, asci)

        # i = 0
        # j = len(s) - 1
        # while i <= j:
        #     left = valid(s[i])
        #     right = valid(s[j])
        #     while not left[0]:
        #         i += 1
        #         if i <= j:
        #             left = valid(s[i])
        #         else:
        #             break
        #     while not right[0]:
        #         j -= 1
        #         if i <= j:
        #             right = valid(s[j])
        #         else:
        #             break
        #     if left[1] != right[1]:
        #         return False
        #     i += 1
        #     j -= 1
                
        # return True


        '''
            Time: O(n)
            Space: O(1)
            NOTE: Using inbuilt libraries
        '''
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True