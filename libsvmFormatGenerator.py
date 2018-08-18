# coding: utf-8

import random
import pandas as pd

#读取文件
flu = pd.read_excel(r'E:\train_data.xlsx',header=None)
flu.columns = ['x1','x2','x3','x4','x5','x6','x7','Y']
for col in flu.columns[:-1]:
    flu[col] = (flu[col] - flu[col].min())/(flu[col].max() - flu[col].min())

#随机分为train和val
testNum = 15
idx = list(range(flu.shape[0]))
random.shuffle(idx)
idx_test = idx[:testNum]
idx_train = idx[testNum:]

#生成libsvm格式的训练集
for i in idx_train:
    sample = '%f 1:%f 2:%f 3:%f 4:%f 5:%f 6:%f 7:%f 8:%f\n' % (flu.iloc[i][-1],
                                             flu.iloc[i][0],flu.iloc[i][1],flu.iloc[i][2],
                                             flu.iloc[i][3],flu.iloc[i][4],flu.iloc[i][5],
                                                               flu.iloc[i][6],flu.iloc[i][7])
    with open(r'E:/train.txt','a+') as ft:
        ft.write(sample)


#生成libsvm格式的验证集
for i in idx_test:
    sample = '%f 1:%f 2:%f 3:%f 4:%f 5:%f 6:%f 7:%f 8:%f\n' % (flu.iloc[i][-1],
                                             flu.iloc[i][0],flu.iloc[i][1],flu.iloc[i][2],
                                             flu.iloc[i][3],flu.iloc[i][4],flu.iloc[i][5],
                                                               flu.iloc[i][6],flu.iloc[i][7])
    with open(r'E:/val.txt','a+') as ft:
        ft.write(sample)

