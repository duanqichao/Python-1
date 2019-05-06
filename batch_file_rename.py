# batch_file_rename.py
# Created: 6th August 2012

"""
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
批量重命名指定目录下面所有文件的后缀名
"""

# just checking
__author__ = 'Craig Richards'
__version__ = '1.0'

import os
import argparse
# argparse 是 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，argparse 将会从 sys.argv 中解析出这些参数，
# 并自动生成帮助和使用信息。当然，Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 docopt，Click。


def batch_rename(work_dir, old_ext, new_ext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    批量重命名指定目录下面所有文件的后缀名
    """
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        # 列出后缀名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # Start of the logic to check the file extensions, if old_ext = file_ext
        # 如果old_ext = file_ext，则启动逻辑以检查文件扩展名
        
        if old_ext == file_ext:
            # Returns changed name of the file with new extention
            ＃返回带有新扩展名的文件名
            newfile = split_file[0] + new_ext

            # Write the files
            # 写入文件
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    """
    This will be called if the script is directly invoked.
    如果直接调用脚本，将调用此方法。
    """
    # adding command line argument
    # 添加命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    # 使用传递的第一个参数设置变量work_dir
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    # 使用传递的第二个参数设置变量old_ext
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    ＃设置变量new_ext，传递第三个参数
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
