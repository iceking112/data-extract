# -*- coding: utf-8 -*-
import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

LTP_DATA_DIR = 'ltp_data'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`

with open('a.txt','r') as f: #读文件
    data = f.read()
# print(data)


segmentor = Segmentor()
segmentor.load(cws_model_path)
words = segmentor.segment(data)
print("|".join(words))
segmentor.release()


postagger = Postagger() # 初始化实例
postagger.load(pos_model_path)  # 加载模型
postags = postagger.postag(words)  # 词性标注
# print('\t'.join(postags))
postagger.release()  # 释放模型


recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型
netags = recognizer.recognize(words, postags)  # 命名实体识别

print('\t'.join(netags))
recognizer.release()  # 释放模型