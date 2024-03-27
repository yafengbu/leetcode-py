#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yafengbu@gmail.com
@Time    :   2024/03/27 11:25:14
@File    :   demo.py
@Usage   :   遍历文件夹
'''

import os


def traverse_folders_with_listdir(path: str, ignore_path: str) -> None:
    # 用 os.listdir 遍历【简单暴力】
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if file in ignore_path:
            # print('ignore:::', file_path)
            pass
        else:
            if os.path.isfile(file_path):
                print(file_path)

            if os.path.isdir(file_path):
                # print(file_path)
                traverse_folders_with_listdir(file_path, '')


def traverse_folders_with_walk(path: str, ignore_path: str) -> None:
    # 用 os.walk 遍历【优雅】
    paths = os.walk(path)

    ignore_path_list = [os.path.join(path, i) for i in ignore_path]
    # print(ignore_path_list, '\n\n')

    for root, dir_lst, file_lst in paths:
        # print(root, dir_lst, file_lst)
        if root in ignore_path_list:
            dir_lst[:] = []  # 忽略当前目录下的子目录

        # 遍历子目录
        # for dir_name in dir_lst:
        #     file_path = os.path.join(root, dir_name)
        #     if root not in ignore_path_list and file_path not in ignore_path_list:
        #         print(root, '\t\t', dir_name, '\t\t', file_path)

        # 遍历所有文件
        for file_name in file_lst:
            file_path = os.path.join(root, file_name)
            if root not in ignore_path_list and file_path not in ignore_path_list:
                print(root, '\t\t', file_name, '\t\t', file_path)


def traverse_folders_with_scandir(path: str) -> None:
    # 用 os.scandir 遍历【高效，但不遍历子目录】
    dirs = []
    files = []
    for item in os.scandir(path):
        # print(item)
        if item.is_dir():
            dirs.append(item.path)
        elif item.is_file():
            files.append(item.path)

    print('dirs::', dirs)
    print('files::', files)


if __name__ == '__main__':
    cur_dir = os.getcwd()
    cur_dir_before = os.path.abspath(os.path.join(cur_dir, '..'))
    cur_dir_before_2_level = os.path.abspath(os.path.join(cur_dir, '..', '..'))
    # print('当前工作的绝对路径:::', cur_dir)
    # print('当前工作路径的上级目录:::', cur_dir_before)
    # print('当前工作路径的上上级目录:::', cur_dir_before_2_level)
    # print()

    path = cur_dir_before
    ignore_path = ['.git', '12-script', 'interview', '.gitignore', 'README.md', 'note.txt', 'demo.py']

    traverse_folders_with_listdir(path, ignore_path)
    # print()
    # traverse_folders_with_walk(path, ignore_path)
    # print()
    # traverse_folders_with_scandir(path)
