
# coding: utf-8

# In[ ]:


import libSVR
def predict():
#     cgp = libSVR.gridregression.gridgregression(r'E:\crack_train_1.txt')
    cgp = {'c': 1024.0, 'g':0.25, 'p': 0.0009765625}
    retPred = libSVR.predict.predict(r'E:\crack_train_1.txt',r'E:\crack_test_1.txt',cgp)
    return retPred

