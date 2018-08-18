# libSVR
This is a package modified from libsvm.
This package can be used to regression task.It can outreach the 
generally machine learnging algorium when the dataset is small and the 
numbers of features are much higher than usually.

Packge need to install :
python 3
libsvm 3.22
numpy
pandas

How to use ?
1. you can use the libsvmFormatGenerator.py to generate the 
needed-format dataset:

 [label] [index1]:[value1] [index2]:[value2] …

 [label] [index1]:[value1] [index2]:[value2] …

label  
目标值，就是可以是数值（回归），或者1 
和-1 class（属于哪一类），就是你要分类的种类，通常是一些整数。

index 是有顺序的索引，通常是连续的整数。就是指特征编号，必须按照升序排列

value 就是特征值，用来train的数据，通常是一堆实数组成

there is an example as follow:

8.200000 1:0.144000 2:0.630000 3:0.774194 4:0.994633 5:0.000000 
6:0.000000 7:0.002793 8:8.200000
8.100000 1:0.500000 2:0.391600 3:0.548387 4:0.488372 5:0.010870 
6:0.006579 7:0.005587 8:8.100000
5.100000 1:0.592000 2:0.326000 3:0.483871 4:0.347048 5:0.010870 
6:0.019737 7:0.033520 8:5.100000
7.800000 1:0.456000 2:0.451600 3:0.322581 4:0.223614 5:0.010870 
6:0.756579 7:0.000000 8:7.800000

you had better to normalize the feature data to [0,1],that turns out to 
be significant for better accuracy.

2. main.py tell you how to use the package.
you can train your data or predict 

3. gridregression.py  is modified from the libsvm.
hte latter version need the command line to input the parameter.In this 
package you can change the parameter in the gridregression.py if you 
need.

