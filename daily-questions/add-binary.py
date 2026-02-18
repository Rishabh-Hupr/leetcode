class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
            https://leetcode.com/problems/add-binary/
            Time: O(n + m)
            Space: O(1)
        '''
        n = len(a) - 1
        m = len(b) - 1
        carry = 0
        ans = []
        while m > -1 and n > -1:
            if a[n] == b[m]:
                if a[n] == "1":
                    if carry == 1:
                        ans.append("1")
                    else:
                        ans.append("0")
                        carry = 1
                else:
                    ans.append(str(carry))
                    carry = 0
            elif carry == 1:
                ans.append("0")
            else:
                ans.append("1")
            m -= 1
            n -= 1
        
        while n > -1:
            if a[n] == "1":
                if carry == 1:
                    ans.append("0")
                else:
                    ans.append(a[n])
            else:
                if carry == 1:
                    ans.append("1")
                    carry = 0
                else:
                    ans.append(a[n])
            n -= 1
        
        while  m > -1:
            if b[m] == "1":
                if carry == 1:
                    ans.append("0")
                else:
                    ans.append(b[m])
            else:
                if carry == 1:
                    ans.append("1")
                    carry = 0
                else:
                    ans.append(b[m])
            m -= 1
        if carry == 1:
            ans.append(str(carry))
        ans.reverse()
        return ''.join(ans)

        n, m = len(a) - 1, len(b) - 1
        carry = 0
        ans = []

        # CHAT GPT SOLUTION
        # while n >= 0 or m >= 0 or carry:
        #     total = carry
            
        #     if n >= 0:
        #         total += int(a[n])
        #         n -= 1
        #     if m >= 0:
        #         total += int(b[m])
        #         m -= 1
            
        #     ans.append(str(total % 2))
        #     carry = total // 2

        # return ''.join(reversed(ans))
