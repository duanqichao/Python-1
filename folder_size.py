# Script Name   : folder_size.py
# Author        : Craig Richards
# Created       : 19th July 2012
# Last Modified	: 22 February 2016
# Version       : 1.0.1

# Modifications : Modified the Printing method and added a few comments

# Description   : This will scan the current directory and all subdirectories and display the size.
# 统计当前文件夹和子文件夹、子文件的大小

import os
import sys      # Load the library module and the sys module for the argument vector'''
                # 加载 os 模块和 sys 模块以获取参数。
try:
    directory = sys.argv[1]   # Set the variable directory to be the argument supplied by user.
                              # 将变量 directory 设置为系统提供的参数。
except IndexError:
    sys.exit("Must provide an argument.")

dir_size = 0    # Set the size to 0
                # 将 dir_size 设置为 0
fsizedicr = {'Bytes': 1,
             'Kilobytes': float(1) / 1024,
             'Megabytes': float(1) / (1024 * 1024),
             'Gigabytes': float(1) / (1024 * 1024 * 1024)}
for (path, dirs, files) in os.walk(directory):      # Walk through all the directories. For each iteration, os.walk returns the folders, subfolders and files in the dir.
                                                    # 遍历目录，每次迭代 os.walk 返回目录中的文件夹，子文件夹和文件。
    for file in files:                              # Get all the files
                                                    # 遍历所有文件
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)       # Add the size of each file in the root dir to get the total size.
                                                    # 累加每个文件的大小以获取总大小。
fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr] # List of units
                                                                                        # 列出所有。

if dir_size == 0: print ("File Empty") # Sanity check to eliminate corner-case of empty file.
                                       # 检查以消除空文件。
else:
  for units in sorted(fsizeList)[::-1]: # Reverse sort list of units so smallest magnitude units print first.
                                        # 按大小反向排序列表。
      print ("Folder Size: " + units)
