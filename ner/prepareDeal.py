# -*- coding: utf-8 -*-

import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from collections import Counter

class PrepareDeal():
    LTP_DATA_DIR = 'ltp_data'  # ltp模型目录的路径

    def __init__(self):
        self.cws_model_path = os.path.join(self.LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        self.pos_model_path = os.path.join(self.LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        self.ner_model_path = os.path.join(self.LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
        segmentor = Segmentor()
        segmentor.load(self.cws_model_path)
        self.words = segmentor.segment(data)
        # print("|".join(words))
        segmentor.release()


        postagger = Postagger() # 初始化实例
        postagger.load(self.pos_model_path)  # 加载模型
        self.postags = postagger.postag(self.words)  # 词性标注
        # print('\t'.join(postags))
        postagger.release()  # 释放模型


        recognizer = NamedEntityRecognizer() # 初始化实例
        recognizer.load(self.ner_model_path)  # 加载模型
        self.netags = recognizer.recognize(self.words, self.postags)  # 命名实体识别
        # print('\t'.join(netags))
        recognizer.release()  # 释放模型


if __name__ == '__main__':
    with open('a.txt','r') as f: #读文件
        data = f.read()
    # print(data)
    ner = PrepareDeal()
    words = ner.words
    postags = ner.postags
    netags = ner.netags
    # for i in range(0, len(netags)):
    #     if netags[i] != 'O':
    #         print(words[i] + netags[i])

    bfile = open('b.txt', 'w')  # 文件写入操作 没有文件创建
    for i in range(0, len(postags)):
        bfile.writelines(words[i] + ' ' + postags[i] + ' ' + netags[i] + '\n')