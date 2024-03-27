#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/27 18:01:25
@File    :   2-链表/2-两数相加.py
@Desc    :   给定两个非空的链表 l1 和 l2。分别用来表示两个非负整数，每位数字都是按照逆序的方式存储的，每个节点存储一位数字。
                要求：计算两个非负整数的和，并逆序返回表示和的链表。
'''

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)  # head:头节点, curr:当前节点指针
        carry = 0
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0

            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0

            sum = num1 + num2 + carry
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

        return head.next


def create_linked_list(nums: List[int]) -> ListNode:
    # 创建链表
    head = ListNode(0)  # 创建一个头节点
    curr = head  # 当前节点指针

    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next

    return head.next  # 返回头节点的下一个节点


def test(l1_list: List[int], l2_list: List[int]) -> ListNode:
    # 测试
    l1 = create_linked_list(l1_list)  # 定义 l1 链表
    l2 = create_linked_list(l2_list)  # 定义 l2 链表

    eg = Solution()
    # 获取返回值的链表
    res_l = eg.addTwoNumbers(l1, l2)

    # 循环遍历出来
    res_list = []
    while res_l:
        # print(res_l.val)
        res_list.append(res_l.val)
        res_l = res_l.next
    print('\nparam::', l1_list, l2_list)
    print('->res::', res_list)


if __name__ == '__main__':
    param_test = [
        {'l1': [2, 4, 3], 'l2': [5, 6, 4]},
        {'l1': [0], 'l2': [0]},
        {'l1': [9, 9, 9, 9, 9, 9, 9], 'l2': [9, 9, 9, 9]},
    ]
    for param in param_test:
        test(param['l1'], param['l2'])

# 解题思路
# l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]  # 解释：342 + 465 = 807
# l1 = [0], l2 = [0] -> [0]

# 参考：https://algo.itcharge.cn/Solutions/0001-0099/add-two-numbers/
# 时间复杂度：O(max(m,n))，   其中，m 和 n 分别是链表 l1 和 l2 的长度。
# 空间复杂度：O(1)

# 模拟大数加法，按位相加，将结果添加到新链表上。需要注意进位和对 10 取余。
