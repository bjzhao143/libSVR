# -*- coding: utf-8 -*-

import sys
sys.path.append('C:\libsvm-3.22\python')
import os
os.chdir('C:\libsvm-3.22\python')       # 请根据实际路径修改

def predict(trainFileName,testFileName,cgp={'c':1024,'g':16,'p':0.015625}):


    from svmutil import svm_read_problem, svm_train, svm_predict

    y, x = svm_read_problem(trainFileName)
    yt, xt = svm_read_problem(testFileName)

    model = svm_train(y, x, '-s 4 -t 2 -c %f -g %f -p %f' % (cgp['c'],cgp['g'],cgp['p']))

    p_label, p_acc, p_val = svm_predict(yt, xt, model)
    return (p_label, p_acc, p_val)



