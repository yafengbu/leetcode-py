#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/26 14:14:43
@File    :   6-字符串/459-重复的子字符串.py
@Desc    :   给定一个非空的字符串 s。检查该字符串 s 是否可以通过由它的一个子串重复多次构成。
'''

from typing import List


class Solution:
    def generateNext(sel, p: str) -> List:
        m = len(p)
        next = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left-1]
            if p[left] == p[right]:
                left += 1
                next[right] = left

        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size == 0:
            return False
        next = self.generateNext(s)
        if next[size-1] != 0 and size % (size-next[size-1]) == 0:
            return True
        return False


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = ['ababab', 'aba', 'abab']
    for param in param_test:
        print(param, '->', eg.repeatedSubstringPattern(param))

# 解题思路
# 'ababab' -> true
# 'aba' -> false

# 参考：https://algo.itcharge.cn/Solutions/0400-0499/repeated-substring-pattern/
# 思路：KMP算法
