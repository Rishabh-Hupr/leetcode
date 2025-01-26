#!/usr/bin/env python3

from math import log
import heapq as hq


first = lambda h: 2**h - 1      # H stands for level height
last = lambda h: first(h + 1)
level = lambda heap, h: heap[first(h):last(h)]
prepare = lambda e, field: str(e).center(field)


def hprint(heap, width=None):
    if width is None:
        width = max(len(str(e)) for e in heap)
    height = int(log(len(heap), 2)) + 1
    gap = ' ' * width
    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))


def findKthLargest(nums, k) -> int:
    # space O(1)
    # time O(n) + O(n) + O(klogn)
    # for i, val in enumerate(nums):
    #     nums[i] = -val
    # hq.heapify(nums)
    # for i in range(k-1):
    #     hq.heappop(nums)
    # return -hq.heappop(nums)
    hps = list()
    for i in range(k):
        hps.append(nums[i])
    hq.heapify(hps)
    n = len(nums)
    for i in range(k, n):
        if nums[i] > hps[0]:
            hq.heapreplace(hps, nums[i])
    hprint(hps)
    return hps[0]

def main():
    # nums = [3,2,1,5,6,4]
    # k = 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    hprint(nums)
    # print(findKthLargest(nums, k))
    # heap_input = something
    # for x in reversed(range(31)):
    #     # e = chr(ord('A') + x)
    #     e = x
    #     heapq.heappush(h, e)
    #     print('Adding {}:'.format(e))
    #     hprint(h)
    #     print()



if __name__ == '__main__':
    main()
