###A1肇事原因圓餅圖###
import pandas as pd
import matplotlib.pyplot as plt

for i in range(2018,2023): # 2018-2022資料
    file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/" # 檔案路徑
    file_name = "" +str(i)+"年度A1交通事故資料.csv"
    f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
    data = pd.read_csv(f)
    data = data.drop_duplicates(subset=['發生地點'])# 刪除重複通報資料
    
    count_data1 = data.groupby(["肇因研判子類別名稱-主要"]).size().reset_index(name="value")# 用groupby算次數
    count_data1 = count_data1.rename(columns={'肇因研判子類別名稱-主要': 'reasons'})# 變更欄名稱
    
    
    count_data1 = count_data1.sort_values(by='value', ascending=False)# sort_values將數值排列, ascending=False將數值按照大排到小, ascending=False
    count_data1 = count_data1.iloc[0:10, [0, 1]]# 取出前10名
   
    # 處理圖片中中文字型
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    # 設定座標軸、標題
    labels = count_data1["reasons"]# 類別標籤
    size = count_data1["value"]# 數值來源
    plt.pie(size, labels = labels, autopct='%1.1f%%')# autopct顯示百分比                 
    plt.axis('equal')                                # 使圓餅圖比例相等
    plt.title(str(i)+'年-A1類車禍肇事原因分佈')
    plt.show()
    plt.close() 