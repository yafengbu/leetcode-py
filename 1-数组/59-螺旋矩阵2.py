#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/28 13:33:06
@File    :   1-数组/59-螺旋矩阵2.py
@Desc    :   给你一个正整数 n，要求：生成一个包含 1∼n^2 的所有元素，且元素按顺时针顺序螺旋排列的 n×n 正方形矩阵 matrix
'''

from typing import List


class Solution:
    def getnerateMatrix(self, n: int) -> List[List[int]]:
        # 构建一个 n×n 大小的数组存储结果
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # 初始边界
        # 顺时针：上-右-下-左
        up, right, down, left = 0, n-1, n-1, 0
        number = 1  # 需要填充的数字

        while left < right and up < down:
            # 从左到右
            for i in range(left, right):
                matrix[up][i] = number
                number += 1

            # 从上到下
            for i in range(up, down):
                matrix[i][right] = number
                number += 1

            # 从右到左
            for i in range(right, left, -1):
                matrix[down][i] = number
                number += 1

            # 从下到上
            for i in range(down, up, -1):
                matrix[i][left] = number
                number += 1

            # 缩小边界
            up += 1
            right -= 1
            down -= 1
            left += 1

            # 如果n为奇数，额外填充一次中心
            if n % 2 == 1:
                # 中心坐标
                mid = n // 2
                matrix[mid][mid] = number

        return matrix


if __name__ == '__main__':
    eg = Solution()
    # 测试
    param_test = [3, 1, 4, 5]
    for param in param_test:
        res = eg.getnerateMatrix(param)
        print('\n', param, '->', res)
        for row in res:
            for i in row:
                print(str(i).rjust(5), end='')
            print()

# 解题思路
# 3 -> [[1,2,3], [8,9,4], [7,6,5]]
# 1 -> [[1]]

# 参考：https://algo.itcharge.cn/Solutions/0001-0099/spiral-matrix-ii/
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

# 思路：顺时针一圈圈填充
