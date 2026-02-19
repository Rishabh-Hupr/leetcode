class Solution:
    def longestBalanced(self, s: str) -> int:
        '''
            https://leetcode.com/problems/longest-balanced-substring-ii
            Time: O(n)
            Space: O(1)
            MY first solution is below
        '''
        n = len(s)
        ans = 0
        
        def check_single(s):
            nonlocal ans
            nonlocal n
            i = 0
            while i < n:
                j = i+1
                while j < n and s[j] == s[i]:
                    j += 1
                ans = max(ans, j - i)
                i = j

        def check_double(s, x, y):
            nonlocal ans
            nonlocal n
            i = 0

            while i < n:
                while i < n and (s[i] != x and s[i] != y):
                    i += 1
                
                j = i
                store = {0 : j-1}
                countX = 0
                countY = 0
                while j < n and (s[j] == x or s[j] == y):
                    if s[j] == x:
                        countX += 1
                    else:
                        countY += 1
                    
                    diff = countX - countY
                    if diff in store:
                        ans = max(ans, j - store[diff])
                    else:
                        store[diff] = j
                    j += 1
                
                i = j
        
        def check_triplet(s):
            nonlocal ans
            nonlocal n

            store = {(0, 0): -1}
            countA = countB = countC = 0
            for i in range(n):
                if s[i] == "a":
                    countA += 1
                elif s[i] == "b":
                    countB += 1
                else:
                    countC += 1
                
                diffAB = countA - countB
                diffAC = countA - countC
                if (diffAB, diffAC) in store:
                    ans = max(ans, i  - store[(diffAB, diffAC)])
                else:
                    store[(diffAB, diffAC)] = i


        check_single(s)
        check_double(s, "a", "b")
        check_double(s, "b", "c")
        check_double(s, "a", "c")
        check_triplet(s)
        return ans

        '''
            Time: O(n^2)
            Space: O(n^2)
            Exceeded time limit at 826th test case out of 1033 test cases
            This solution implemented cache with recursive backtracking to check all possible substring and check if they are balanced or not.
            and exit early if we find a balanced substring and skip the recursive check on the rest of the substring that is contained in the balanced substring.
        '''
        # n = len(s)
        # l = 0
        # r = n - 1

        # counterMap = Counter(s)
        # ans = 0
        # cache = dict()

        # def recursionCheck(s, l, r):
        #     nonlocal ans
        #     if l <= r:
        #         if (l, r) in cache:
        #             return cache[(l, r)]
        #         tmp = 0
        #         # check current string from l to r
        #         if checkBalanced(counterMap):
        #             ans = max(r - l + 1, ans)
        #             return ans
                
        #         # skip the l and then check the rest from l+1 to r
        #         counterMap[s[l]] -= 1
        #         l += 1
        #         cache[(l, r)] = recursionCheck(s, l ,r)
        #         tmp = max(cache[(l, r)], tmp)

        #         # if skipping with l didn't find anything, then search from l to r-1
        #         # re-gain l
        #         l -= 1
        #         counterMap[s[l]] += 1

        #         # remove r and then recursionCheck again
        #         counterMap[s[r]] -= 1
        #         r -= 1
        #         cache[(l, r)] = recursionCheck(s, l, r)
        #         tmp = max(cache[(l, r)], tmp)
                
        #         # re-gain r as well
        #         r += 1
        #         counterMap[s[r]] += 1
        #         return tmp


        # def checkBalanced(counterMap):
        #     values = iter(val for val in counterMap.values() if val != 0)
        #     first = next(values, None)
        #     return all(val == first for val in values)

        # recursionCheck(s, l, r)
        # return ans