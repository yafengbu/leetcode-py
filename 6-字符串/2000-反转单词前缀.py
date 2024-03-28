#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/28 21:25:38
@File    :   6-字符串/2000-反转单词前缀.py
@Desc    :   给你一个字符串 word 和一个字符 ch ，
    找出 ch 第一次出现的下标 i ，反转 word 中从下标 0 开始、直到下标 i 结束（含下标 i ）的那段字符。
    如果 word 中不存在字符 ch ，则无需进行任何操作。

    例如，如果 word = "abcdefd" 且 ch = "d" ，那么你应该 反转 从下标 0 开始、直到下标 3 结束（含下标 3 ）。
    结果字符串将会是 "dcbaefd" 。
'''


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)

        # 如果 word 中不存在字符 ch
        if i < 0:
            return word

        return word[i::-1] + word[i+1:]


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [
        {'word': 'abcdefd', 'ch': 'd'},
        {'word': 'xyxzxe', 'ch': 'z'},
        {'word': 'abcd', 'ch': 'z'},
    ]
    for param in param_test:
        print(param, '->', eg.reversePrefix(param['word'], param['ch']))

# 解题思路
# word = 'abcdefd', ch = 'd' -> 'dcbaefd'
# word = 'xyxzxe', ch = 'z' -> 'zxyxxe'
# word = 'abcd', ch = 'z' -> 'abcd'
