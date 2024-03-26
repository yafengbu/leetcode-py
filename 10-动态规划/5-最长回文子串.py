#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/26 13:25:22
@File    :   10-动态规划/5-最长回文子串.py
@Desc    :   回文串：如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # dp[i][j] 表示为：字符串 s 在区间 [i,j] 范围内是否是一个回文串。
        # 初始状态：默认字符串 s 的所有子串都不是回文串
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_start = 0
        max_len = 1

        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and (j-i+1) > max_len:
                    max_len = j-i+1
                    max_start = i
        return s[max_start: max_start+max_len]


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = ['babad', 'cbbd', 'ab', 'bb']
    for param in param_test:
        print(param, '->', eg.longestPalindrome(param))

# 解题思路
# 'babad' -> 'bab'
# 'ab' -> 'a'

# 参考： https://algo.itcharge.cn/Solutions/0001-0099/longest-palindromic-substring/
