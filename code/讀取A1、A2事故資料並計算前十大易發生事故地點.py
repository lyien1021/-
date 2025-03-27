###讀取A1、A2事故資料並計算前十大易發生事故地點###
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

combined = pd.DataFrame()
fouryears = pd.DataFrame()
combinedA1 = pd.DataFrame()

for a in range(2018,2022):
    print(a)
    for i in range(1,13): # 1月-12月資料
        print(i)
        file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/"+str(a)+"年傷亡道路交通事故資料/" # 檔案路徑
        file_name = ""+str(a)+"年度A2交通事故資料_"+str(i)+".csv"
        f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
        data = pd.read_csv(f)
        data = data.drop_duplicates(subset=['發生時間','發生地點'])# 刪除重複通報資料(改良後用時間加地點篩選)
        combined = combined.append(data)# 組合起來存到conbined裡面
    fouryears = fouryears.append(combined)        
count_data_A2 = fouryears.groupby(["發生地點"]).size().reset_index(name="value")   
count_data_A2 = count_data_A2.rename(columns={'發生地點': 'A2發生地點'})    

for b in range(2018,2022): # 2018-2021資料
    print(b)    
    file_src = "C:/Users/ann90/OneDrive/桌面/作業/python資料分析/期中報告/期中報告/" # 檔案路徑
    file_name = "" +str(b)+"年度A1交通事故資料.csv"
    f = open(file_src + file_name,encoding="utf-8")# encoding="utf-8"告訴python文件的編碼才讀得出來
    a1data = pd.read_csv(f)
    a1data = a1data.drop_duplicates(subset=['發生時間','發生地點'])# 刪除重複通報資料(改良後用時間加地點篩選)
    combinedA1 = combinedA1.append(a1data)
    #combinedA1_2 = combinedA1[['發生地點','經度', '緯度']]
count_data_A1 = combinedA1.groupby(["發生地點"]).size().reset_index(name="valueA1")
count_data_A1 = count_data_A1.rename(columns={'發生地點': 'A1發生地點'})    

    
count_data_A1 = count_data_A1.sort_values(by='valueA1', ascending=False)# sort_values將數值排列, ascending=False將數值按照大排到小
count_data_A1 = count_data_A1.iloc[0:10, [0, 1]] 
count_data_A2 = count_data_A2.sort_values(by='value', ascending=False)# sort_values將數值排列, ascending=False將數值按照大排到小
count_data_A2 = count_data_A2.iloc[0:10, [0, 1]] 
count_data_A1.reset_index(inplace=True)
count_data_A2.reset_index(inplace=True)
count_data = count_data_A1.join(count_data_A2,lsuffix='A1',rsuffix='A2').drop(['indexA1','indexA2'],axis=1)



