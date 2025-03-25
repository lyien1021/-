###A1事故肇事者年齡圓餅圖###

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from collections import Counter

for i in range(2018,2023): #2018-2022資料
    file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/"# 檔案路徑
    file_name = "" +str(i)+"年度A1交通事故資料.csv"
    f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
    data = pd.read_csv(f)
    data = data.drop_duplicates(subset=['發生地點'])# 刪除重複通報資料
    
    range=[0,18,26,40,65,np.inf] # 年齡範圍制定
    group=['kid','young','grow','mid','old'] #按年齡範圍標籤
    data['age_type']=pd.cut(data['當事者事故發生時年齡'],bins=range,labels=group)
    count_data1 = data.groupby(["age_type"]).size().reset_index(name="value")
    
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    labels = count_data1["age_type"]# 類別標籤
    size = count_data1["value"]# 數值來源
    plt.pie(size, labels = labels, autopct='%1.1f%%')# autopct顯示百分比                 
    plt.axis('equal')                                # 使圓餅圖比例相等
    plt.title(str(i)+'年-A1類車禍肇事年齡區間')
    plt.show()
    plt.close()
    