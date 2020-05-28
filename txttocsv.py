
import numpy as np  
import pandas as pd  
  
txt = pd.read_table('./dataset/Gowalla_totalCheckins.txt')  
txtDF = pd.DataFrame(txt)  
txtDF.to_csv('./dataset/Gowalla_totalCheckins.csv',index=False)