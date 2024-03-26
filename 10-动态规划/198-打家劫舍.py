#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/26 14:20:45
@File    :   10-动态规划/198-打家劫舍.py
@Desc    :   题目大意：给定一个数组 nums，nums[i] 代表第 i 间房屋存放的金额。相邻的房屋装有防盗系统，假如相邻的两间房屋同时被偷，系统就会报警。
                    要求：假如你是一名专业的小偷，计算在不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。
'''

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # 状态 dp[i] 表示为：前 i 间房屋所能偷窃到的最高金额。
        dp = [0 for _ in range(size+1)]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, size+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])

        return dp[size]


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [[1, 2, 3, 4], [1, 2, 3, 1], [2, 7, 9, 3, 1]]
    for param in param_test:
        print(param, '->', eg.rob(param))

# 解题思路
# 列表不相邻元素，求和最大值
# [1, 2, 3, 4] -> 6

# 参考：https://algo.itcharge.cn/Solutions/0100-0199/house-robber/
