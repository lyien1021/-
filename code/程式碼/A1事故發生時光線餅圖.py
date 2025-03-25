###A1事故發生時光線餅圖###

import pandas as pd
import matplotlib.pyplot as plt

for b in range(2018,2022): # 2018-2021資料
    print(b)    
    file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/" # 檔案路徑
    file_name = "" +str(b)+"年度A1交通事故資料.csv"
    f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
    data = pd.read_csv(f)
    data = data.drop_duplicates(subset=['發生地點','發生時間'], keep='last')# 刪除重複通報資料
                                      
    count_data1 = data.groupby(["肇因研判子類別名稱-主要"]).size().reset_index(name="value")# 用groupby算次數
    count_data1 = count_data1.rename(columns={'肇因研判子類別名稱-主要': 'reasons'})# 變更欄名稱
    
    # sort_values將數值排列, ascending=False將數值按照大排到小, ascending=False
    count_data1 = count_data1.sort_values(by='value', ascending=False)
    count_data1 = count_data1.iloc[0:10, [0, 1]]# 取出前10名
    count_data1 = count_data1.sort_values(by='value')# 再重新排列，使最大值出現在最上面
    
    #光線圓餅圖
    count_data2 = data.groupby(["光線名稱"]).size().reset_index(name="value")# 用groupby算次數
    count_data2 = count_data2.rename(columns={'光線名稱': 'light'})# 變更欄名稱
    # sort_values將數值排列, ascending=False將數值按照大排到小, ascending=False
    count_data2 = count_data2.sort_values(by='value', ascending=False)
    #count_data2 = count_data2.iloc[0:10, [0, 1]]# 取出前10名
    count_data2 = count_data2.sort_values(by='value')# 再重新排列，使最大值出現在最上面
    
    plt.figure(figsize=(6,9))
    labels = count_data2["light"]
    size = count_data2["value"]
    plt.pie(size,                           # 數值
        labels = labels,                # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        colors = ['brown', 'yellow','y', 'orange'],
        pctdistance = 0.6,              # 數字距圓心的距離
        textprops = {"fontsize" : 12},  # 文字大小
        shadow=False)                    # 設定陰影
    plt.title("2018~2021 light situation of the accidents", {"fontsize" : 18})  # 設定標題及其文字大小
    

    
# #input image
# import matplotlib.image as img
# import os
# os.chdir('C:/Users/ann90/OneDrive/桌面/作業/python資料分析/data/')   # 如果是用 Colab 需要改變路徑
# image = img.imread('taiwan.png')                       # 讀取圖片
# plt.imshow(image)                                    # 在圖表中繪製圖片
# plt.show()       