# -*- coding: UTF-8 -*-
import numpy as np
######  第四章           Numpy学习
#######
##当high为默认值时，low为最大值
data = np.random.randint(7,high=19,size = (3,4),dtype=np.uint8)
print(data)
data = np.random.randint(4,size=(3,4),dtype=int)
print(data)
print(10*data)
print('shape = '+str(data.shape))

###python数组作为参数创建ndarray
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
print(str(arr2.ndim)+str(arr2.shape))

####特殊生成ndarray方法shape, dtype=None, order='C'
print(np.ones((2,2),dtype=int))
print(np.zeros((2,2),dtype=int))

###dtype转换，将浮点数转换成整数，则小数点后面的部分将被消除
arr = np.array([1,2,3,4])
print(arr.dtype)
float_arr = np.array([3.4,5.6,7.3])
print(float_arr.dtype)
int_arr = float_arr.astype(np.int32)
print(float_arr)
print(int_arr)

##字符串转化为数字
str_arr = np.array(['1.1','2.2','3.3'])
number_arr = str_arr.astype(float)
print(number_arr)

###numpy数组算术
data3 = data*data
print(data3)
data4 = data-data
print(data4)
##一元函数
data = np.array([[2,3,4,5,],[7,8,9,6]])
data4 = np.log(data)
print(data4)
print(np.sqrt(data))
print(np.cos(data))

######################################################################
#############基础索引与切片############################################
################一维数组,切片返回的是视图,改变视图也会反映到原数组上#####
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
print(arr)

arr[5]= 999
print(arr)
arr[5:8][0] = 777
print(arr)

##更高纬度数组中，每个索引值不再是一个值，而是一个一维数组
arr2d = np.arange(9)
arr2d = arr2d.reshape(3,3)
print(arr2d)
arr2d[1] = 111
print(arr2d)

arr3d = np.arange(30)
arr3d = arr3d.reshape(2,3,5)
print(arr3d)
print(arr3d[0])
#arr3d[0][1][0:3] = 999
#print(arr3d)
##选择第一个二维数组的前3列
print(arr3d[0][0:,:3])
print(arr3d[0,0:,:3])

#######################布尔索引


#######################神奇索引
#######################神奇索引与切片不同，它总是将数据复制到一个新的数组中
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)
arry1 = arr[[4,3,0,6]]
print(arry1)
##使用负的索引，从尾部选择
arry2 = arr[[-1,-3,-5]]
print(arry2)
##选择(1,0),(5,3),(7,1),(2,2)
arr = np.arange(32).reshape((8,4))
arry3 = arr[[1,5,7,2],[0,3,1,2]]
print(arry3)

####数组的转置和换轴
####转置是一种特殊的数组重组形式，可以返回底层数据的视图而不需要复制任何内容。数组拥有transpose
####方法，也有特殊的T属性(就是矩阵的转置)
arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)
#######计算数组的内积,randn表示随机正态分布
arr = np.random.randn(3,6)
arrd = np.dot(arr,arr.T)
print(arrd)

####更高维度的数组transpose方法接收包含轴编号的元祖,用于置换轴
###transpose() @param:shape()参数的索引
###三维数组就是(0,1,2),transpose(0,1,2)就是没有做任何改变
###swapaxes()方法将两个维度进行转置
arr = np.arange(16).reshape((2,2,4))
arr_t = arr.transpose((1,0,2))
print(arr_t)
print(arr)
print(arr.swapaxes(1,2))


#######通用函数ufunc,逐元素替换函数
#一元函数
##    函数名
##    abs fbs
#    sqrt
#    square
#    exp
##    log/log10/log2/log1p
##    sign
##    ceil
##    floor
##    rint
##    modf
##    isnan
##    isfinite/isinf
##    cos/cosh/sin
##    sinh/tan/tanh
##   arccos/arccosh/arcsin
##    arcsinh/arctan/arctanh
##    logical_not

####################################################################################







