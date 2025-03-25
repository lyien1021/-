###A1事故肇事原因長條圖###
import pandas as pd
import matplotlib.pyplot as plt

for i in range(2018,2023): # 2018-2022資料
    print(i)    
    file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/" # 檔案路徑
    file_name = "" +str(i)+"年度A1交通事故資料.csv"
    f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
    data = pd.read_csv(f)
    data = data.drop_duplicates(subset=['發生時間','發生地點'])# 刪除重複通報資料(改良後用時間加地點篩選)
    

    count_data = data.groupby(["肇因研判子類別名稱-主要"]).size().reset_index(name="value")# 用groupby算次數
    count_data = count_data.rename(columns={'肇因研判子類別名稱-主要': 'reasons'})# 變更欄名稱
    
    
    count_data = count_data.sort_values(by='value', ascending=False)# sort_values將數值排列, ascending=False將數值按照大排到小
    count_data = count_data.iloc[0:10, [0, 1]]# 取出前10名
    count_data = count_data.sort_values(by='value')# 再重新排列，使最大值出現在圖最上面
   
    # 中文字型顯示設定
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    # 設定座標軸、標題
    plt.ylabel('肇事原因')# y軸肇事原因
    plt.xlabel('統計次數')# x軸肇事原因統計次數
    plt.title(str(i)+'年-A1類車禍肇事原因統計')
    barplot = plt.barh(count_data.reasons, count_data.value)# 畫直方圖
    plt.bar_label(barplot,labels =count_data.value,label_type='edge' )# 標示次數
    # a = i-2016
    # plt.subplot(2,3,a)
    # plt.tight_layout()
    plt.show()
    plt.close()
    
    
    
    