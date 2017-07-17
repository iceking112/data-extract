# -*- coding: utf-8 -*-

import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from collections import Counter

class Ner():
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

    # 获取姓名
    def identifyingNames(self,words,netags):
        if netags[0] == 'S-Nh':
            return words[0]
        else:
            names = []
            for i in range(0, len(netags)):
                if netags[i] == 'S-Nh':
                    names.append(words[i])
            # 取出现次数最多的姓名
            return Counter(names).most_common(1).pop(0)[0]
            # 获取姓名
    def getCount(self,list,key):
        if list.get(key) != None:
            return list.get(key)
        else:
            return 0

    # 获取性别
    def identifyingSex(self, words, netags):
        wordList = Counter(words)
        if '性别' in words:
            for i in range(0, len(words)):
                if words[i] == '性别':
                    for j in range(i, i+3):
                        if words[j] == '男' or words[j] == '女':
                            return words[j]
        elif '男' in words and '女' not in words:
            return '男'
        elif '女' in words and '男' not in words:
            return '女'
        elif self.getCount(wordList, '他') > self.getCount(wordList,'她'):
            return '男'
        elif self.getCount(wordList, '他') < self.getCount(wordList,'她'):
            return '女'
        else:
            return '男'

if __name__ == '__main__':
    with open('a.txt','r') as f: #读文件
        data = f.read()
    # print(data)
    ner = Ner()
    words = ner.words
    netags = ner.netags
    # for i in range(0, len(netags)):
    #     if netags[i] != 'O':
    #         print(words[i] + netags[i])

    name = ner.identifyingNames(words, netags)
    print(name)
    sex = ner.identifyingSex(words, netags)
    print(sex)