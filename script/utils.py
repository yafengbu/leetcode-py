#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/27 16:29:11
@Usage   :   工具脚本
'''

import re


def extract_number(s: str) -> int:
    # 从字符串中提取数字
    # num = s.split('-')[0]
    num = re.search(r'\d+', s).group()  # 正则匹配数字，更高级
    # print(s, '->', num)
    return int(num)


if __name__ == '__main__':
    # 测试
    param_test = ['1-数组', '2-链表', '3-堆栈', '4-队列', '5-哈希表', '6-字符串', '7-树', '8-图', '9-基础算法', '10-动态规划']
    for param in param_test:
        print(param, '->', extract_number(param))
