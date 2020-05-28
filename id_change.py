import numpy as np
import pandas as pd
submit1_path="./dataset/test.csv"
submit1=pd.read_csv(submit1_path)

arr = np.array(submit1)
arr_ = arr[:,0] #取原数据中的第一列序号
arr__ = list(set(arr_)) #每个序号有多个，进行消重

for index, value in enumerate(arr__): #根据消重后的序号进行序号压缩range（0，len（），1）
    for i in range(len(arr_)):
        if arr_[i] == value:
            arr_[i] = index
for i in range(len(arr_)):
    arr[i][0] = arr_[i]

arr = arr[:,0:5]
arr = np.delete(arr, 1, axis=1)
submit_ = pd.DataFrame(arr)
submit_.to_csv("./dataset/test.csv",index=None,header=None)