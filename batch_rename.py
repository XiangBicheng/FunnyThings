import os, sys

dir_path = os.path.dirname(os.path.abspath(__file__))
replace_string = sys.argv[1]

def rename(path, file_or_dir):
    newname = file_or_dir.replace(replace_string, '')
    src_path = os.path.join(path, file_or_dir)
    dst_path = os.path.join(path, newname)
    os.rename(src_path, dst_path)
    return dst_path

def batch_rename(path):
    for file_or_dir in os.listdir(path):
        if file_or_dir == '.vscode' or file_or_dir == 'batch_rename.py':
            continue
        elif os.path.isdir(os.path.join(path, file_or_dir)):
            if replace_string in file_or_dir:
                batch_rename(rename(path, file_or_dir))
            else:
                batch_rename(os.path.join(path, file_or_dir))
        else:
            if replace_string in file_or_dir:
                rename(path, file_or_dir)

batch_rename(dir_path)

# 1. os.path.abspath()函数只会在传入的参数如"file.txt"前加上当前脚本文件的
#    路径，因此需要使用os.path.join函数，保证每次传入batch_rename的都是绝对路径
