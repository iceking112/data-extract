# -*- coding: utf-8 -*-

import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from collections import Counter

class PrepareDeal():
    LTP_DATA_DIR = 'ltp_data'  # ltp模型目录的路径

    def __init__(self):
        pass


if __name__ == '__main__':
    lines = []
    with open('c.txt','r') as f: #读文件
        line = f.readline()
        while line:
            lines.append(line.strip().split(' '))
            line = f.readline()
    print(lines)

    for i in range(0, len(lines)):
        # 如果一行内容有3个词则是正确情况，具体数字具体分析
        if(len(lines[i]) != 3):
            print(lines[i])
            print('第',i+1,'行有问题')