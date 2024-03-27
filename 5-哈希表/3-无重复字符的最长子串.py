#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/27 19:10:57
@File    :   5-哈希表/3-无重复字符的最长子串.py
@Desc    :   给定一个字符串 s，找出其中不含有重复字符的最长子串的长度（s 由英文字母、数字、符号和空格组成）
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = dict()
        res = 0

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)
            right += 1

        return res


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = ['abcabcbb', 'bbbbb', 'pwwkew']
    for param in param_test:
        print(param, '->', eg.lengthOfLongestSubstring(param))

# 解题思路
# 'abcabcbb' -> 3  # 'abc'
# 'bbbbb' -> 1  # 'b'

# 参考：https://algo.itcharge.cn/Solutions/0001-0099/longest-substring-without-repeating-characters/
# 思路：滑动窗口（不定长度）
