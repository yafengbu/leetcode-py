#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/27 17:05:39
@File    :   1-数组/1-两数之和.py
@Desc    :   给定一个整数数组 nums 和一个整数目标值 target。
                要求：在该数组中找出和为 target 的两个整数，并输出这两个整数的下标。可以按任意顺序返回答案。
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 方法一：枚举算法
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j and nums[i]+nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 方法二：哈希表
        numDict = dict()
        for i in range(len(nums)):
            if target-nums[i] in numDict:
                return [numDict[target-nums[i]], i]
            numDict[nums[i]] = i
        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        # 方法三：
        for i in range(len(nums)):
            diff_target = target-nums[i]
            tmp_nums = nums[i+1:]
            if diff_target in tmp_nums:
                return [i, tmp_nums.index(diff_target)+i+1]
        return []


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [
        {'nums': [2, 7, 11, 15], 'target': 9},
        {'nums': [3, 2, 4], 'target': 6},
        {'nums': [3, 3], 'target': 6},
        {'nums': [3, 4, 2, 1], 'target': 8},
    ]
    for param in param_test:
        print(param, '->', eg.twoSum(param['nums'], param['target']))

# 解题思路
# nums = [2,7,11,15], target = 9  -> [0,1]
# nums = [3,2,4], target = 6  -> [1,2]

# 参考：https://algo.itcharge.cn/Solutions/0001-0099/two-sum/
# 思路1：枚举算法
# 时间复杂度：O(n^2)，其中 n 是数组 nums 的元素数量。
# 空间复杂度：O(1)。
#
# 思路2：哈希表
# 时间复杂度：O(n)，其中 n 是数组 nums 的元素数量。
# 空间复杂度：O(n)。
