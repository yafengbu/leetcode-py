#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/28 20:50:28
@File    :   5-哈希表/128-最长连续序列.py
@Desc    :   给定一个未排序的整数数组 nums。
                要求：找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。并且要用时间复杂度为 O(n) 的算法解决此问题。
'''

from typing import List


class Solution:
    def longestConsecutiveSequence(self, nums: List[int]) -> int:
        res = 0
        # 去重
        nums_set = set(nums)

        for num in nums_set:
            # 如果 num-1 存在在 set 中，则 num 不能作为起点，直接跳过
            if num-1 not in nums_set:
                cur = 1  # 当前连续序列长度

                # 循环判断 num+1 是否在 set 中
                while num+1 in nums_set:
                    cur += 1  # 当前连续序列长度+1
                    num += 1
                res = max(res, cur)

        return res


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    ]
    for param in param_test:
        print(param, '->', eg.longestConsecutiveSequence(param))

# 解题思路
# nums = [100,4,200,1,3,2] -> 4  # 最长数字连续序列是 [1, 2, 3, 4]
# nums = [0,3,7,2,5,8,4,6,0,1] -> 9

# 参考：https://algo.itcharge.cn/Solutions/0100-0199/longest-consecutive-sequence/
# 思路：哈希表
