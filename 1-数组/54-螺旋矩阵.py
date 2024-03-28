#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/28 15:46:39
@File    :   1-数组/54-螺旋矩阵.py
@Desc    :   给定一个 m×n 大小的二维矩阵 matrix，要求：按照顺时针旋转的顺序，返回矩阵中的所有元素。
'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List:
        # 边界
        up, left, down, right = 0, 0, len(matrix)-1, len(matrix[0])-1

        res = []
        while True:
            # 从左到右
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1  # 缩小边界
            if up > down:
                break

            # 从上到下
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1  # 缩小边界
            if right < left:
                break

            # 从右到左
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1  # 缩小边界
            if down < up:
                break

            # 从下到上
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1  # 缩小边界
            if left > right:
                break
        return res


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [2, 5, 8],
            [4, 0, -1]
        ]
    ]
    for param in param_test:
        for row in param:
            for i in row:
                print(str(i).rjust(5), end='')
            print()
        print('res ->', eg.spiralOrder(param), '\n')

# 解题思路
# [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]] -> [1,2,3,4,8,12,11,10,9,5,6,7]

# 参考：https://algo.itcharge.cn/Solutions/0001-0099/spiral-matrix/
# 时间复杂度：O(m×n)，其中 mmm、nnn 分别为二维矩阵的行数和列数。
# 空间复杂度：O(m×n)，如果算上答案数组的空间占用，则空间复杂度为 O(m×n)。不算上则空间复杂度为 O(1)。
