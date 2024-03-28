#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/28 17:06:56
@File    :   6-字符串/392-判断子序列.py
@Desc    :   给定字符串 s 和 t，判断 s 是否为 t 的子序列。
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        i, j = 0, 0
        while i < size_s and j < size_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == size_s


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [
        {'s': 'abc', 't': 'ahbgdc'},
        {'s': 'axc', 't': 'ahbgdc'}
    ]
    for param in param_test:
        print(param, '->', eg.isSubsequence(param['s'], param['t']))

# 解题思路
# s = "abc", t = "ahbgdc" -> True
# s = "axc", t = "ahbgdc" -> False

# 参考：https://algo.itcharge.cn/Solutions/0300-0399/is-subsequence/
# 时间复杂度：O(n+m)，其中 n、m 分别为字符串 s、t 的长度。
# 空间复杂度：O(1)

# 解题思路：双指针
# 使用两个指针 i、j 分别指向字符串 s 和 t，然后对两个字符串进行遍历。
# 遇到 s[i]==t[j] 的情况，则 i 向右移。
# 不断右移 j。
# 如果超过 s 或 t 的长度则跳出。
# 最后判断指针 i 是否指向了 s 的末尾，即：判断 i 是否等于 s 的长度。如果等于，则说明 s 是 t 的子序列，如果不等于，则不是。
