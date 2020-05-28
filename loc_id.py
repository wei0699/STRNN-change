import numpy as np
import pandas as pd

#向下设置精度函数,保留四位小数
def precision_down(x):
    x = float(int(x * 10000)) / 10000
    return x

#向上设置精度函数,保留四位小数
def precision_up(x):
    x = float(int(x * 10000 + 1)) / 10000
    return x


file_path="./dataset/test.csv"
date_no_loc=pd.read_csv(file_path)

arr = np.array(date_no_loc) #DataFrame格式转化为array数组

#分别取经度和纬度所在列
arr_longi = arr[:,2:3]
arr_lati = arr[:,3:4]

#数据转换为数值，便于排序
for i in range(len(arr)):
    arr_longi[i] = float(arr_longi[i])
    arr_lati[i] = float(arr_lati[i])

#array格式转化为list，使用用sort函数
arr_longi_list = list(arr_longi)
arr_lati_list = list(arr_lati)

#经度排序取最大最小值
arr_longi_list.sort(reverse=True)
arr_longs_max = arr_longi_list[0]
arr_longi_list.sort(reverse=False)
arr_longs_min = arr_longi_list[0]

#纬度排序
arr_lati_list.sort(reverse=True)
arr_lats_max = arr_lati_list[0]
arr_lati_list.sort(reverse=False)
arr_lats_min = arr_lati_list[0]

#根据需要划分的区域大小设置精确度，这里保留小数点后4位。
#精度每变化0.0001，距离变化10米，纬度每变化0.0001，距离变化11米
#这里忽略经纬度之间的差异，以0.0001为单位划分区域
arr_longs_max = precision_up(arr_longs_max)
arr_longs_min = precision_down(arr_longs_min)
arr_lats_max = precision_up(arr_lats_max)
arr_lats_min = precision_down(arr_lats_min)

#横向分割数
rows = (arr_longs_max - arr_longs_min) / 0.0001
cols = (arr_lats_max - arr_lats_min) / 0.0001
locs_of_1 = int(rows * cols)

#定义用于存储loc_id的array
arr_loc = np.array(np.zeros((len(arr), 1))).astype(int)

for i in range(len(arr)):
    nums = int((arr[i][2] - arr_longs_min) / 0.0001)
    lines = int((arr[i][3] - arr_lats_min) / 0.0001)
    loc_id = int(lines * rows + nums)
    arr_loc[i][0] = loc_id

arr = np.hstack((arr, arr_loc))

submit_ = pd.DataFrame(arr)
submit_.to_csv("./dataset/test.txt",sep='\t',index=None,header=None)