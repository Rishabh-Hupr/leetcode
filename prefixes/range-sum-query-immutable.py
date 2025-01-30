class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        tmp = 0
        for i in nums:
            tmp += i
            self.prefix.append(tmp)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)