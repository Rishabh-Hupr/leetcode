class ProductOfNumbers:
    '''
        https://leetcode.com/problems/product-of-the-last-k-numbers/
        Time: Amortized(1) for add() and O(1) for getProduct()
        Space: O(n)
    '''
    # def __init__(self):
    #     self.lst = []
    #     self.cnt = 0
    #     self.last_zero = -1

    # def add(self, num: int) -> None:
    #     if self.cnt:
    #         if num:
    #             self.lst.append(
    #                 num * self.lst[self.cnt - 1]
    #             )
    #         else:
    #             self.lst.append(
    #                 self.lst[self.cnt - 1]
    #             )
    #             self.last_zero = self.cnt

    #     else:
    #         if num:
    #             self.lst.append(
    #                 num
    #             )
    #         else:
    #             self.lst.append(
    #                 1
    #             )
    #             self.last_zero = self.cnt
    #     self.cnt += 1

    # def getProduct(self, k: int) -> int:
    #     if self.cnt == 1:
    #         return self.lst[0]
    #     x = self.cnt - k - 1
    #     if x < self.last_zero:
    #         return 0
    #     else:
    #         if self.cnt == k:
    #             return self.lst[-1]
    #         return self.lst[self.cnt - 1] // self.lst[x]
    

    '''
        Time: Amortized(1) for add() and O(1) for getProduct()
        Space: O(n) but optimized in the sense that we discard the array when we hit zero(0)
    '''
    def __init__(self):
        self.lst = [1]

    def add(self, num: int) -> None:
        if num:
            self.lst.append(
                self.lst[-1] * num
            )
        else:
            self.lst = [1]

    def getProduct(self, k: int) -> int:
        if k == len(self.lst) - 1:
            return self.lst[-1]
        elif k > len(self.lst) - 1:
            return 0
        else:
            return self.lst[-1] // self.lst[- k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)