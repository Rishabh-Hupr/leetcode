class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
            https://leetcode.com/problems/plus-one/description/
            Time: O(n)
            Space: O(1)
        '''
        # car = 1
        # n = len(digits)
        # for i in range(n-1, -1, -1):
        #     s = digits[i] + car
        #     if s > 9:
        #         car = 1
        #     else:
        #         car = 0
        #     digits[i] = s%10
        # if car:
        #     digits.insert(0, car)
        # return digits

        '''
            Time: O(n^2)
            Space: O(n)
            STILL IT PERFORMS BETTER, NO IDEA WHY
        '''
        st=''
        new=[]
        for i in digits:
            st=st+str(i)
        k=int(st)+1
        for i in str(k):
            new.append(int(i))
        return new