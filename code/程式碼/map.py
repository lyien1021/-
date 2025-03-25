
import folium
m = folium.Map(location=[25.08021833754078, 121.45544482102216],
               zoom_start=8, width=600,height=600, zoom_control='False',attr='AutoNavi')


# popup = folium.Popup(max_width='100%')
folium.Marker(location=[25.075385, 121.458371], 
            tooltip='地址：新北市五股區疏洪一路前0.0公尺'+'<br>'+'發生A1事故次數：5'+'<br>'+'總死傷人數：死亡5人,受傷2人', 
            icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.186546, 121.585603], tooltip="地址：新北市金山區臺2甲線道路前0.0公尺"+'<br>'+'發生A1事故次數：4'+'<br>'+'總死傷人數：死亡4人,受傷6人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.108417, 121.535354], tooltip='地址：臺北市士林區仰德大道1段前0.0公尺'+'<br>'+'發生A1事故次數：4'+'<br>'+'總死傷人數：死亡4人,受傷1人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.901738, 121.720231], tooltip='地址：新北市坪林區北宜公路前0.0公尺'+'<br>'+'發生A1事故次數：4'+'<br>'+'總死傷人數：死亡4人,受傷1人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.022253, 121.485541], tooltip='地址：新北市板橋區環河西路4段前0.0公尺'+'<br>'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷2人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.035768, 120.592046], tooltip='地址：彰化縣芬園鄉舊社村大彰路5段前0.0公尺'+'<br>'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷0人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.033810, 121.493253], tooltip='地址：臺北市萬華區環河南路2段 / 臺北市萬華區環河南路2段'+'<br>'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷0人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.035301, 121.499346], tooltip='地址：臺北市萬華區西園路1段 / 臺北市萬華區和平西路3段'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷1人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.981379, 121.438912], tooltip='地址：新北市土城區擺接堡路前0.0公尺'+'<br>'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷2人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.950000, 121.350000], tooltip='地址：新北市鶯歌區堤外道路前0.0公尺'+'<br>'+'發生A1事故次數：3'+'<br>'+'總死傷人數：死亡3人,受傷4人', icon=folium.Icon(color='red', icon="fa-solid fa-location-pin")).add_to(m)

folium.Marker(location=[25.0691, 121.593], 
            tooltip='地址：臺北市內湖區民權東路6段 / 臺北市內湖區民權東路6段'+'<br>'+'發生A2事故次數：947'+'<br>'+'總死傷人數：死亡5人,受傷2人', 
            icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.040816, 121.574006], tooltip="地址：臺北市信義區忠孝東路5段 / 臺北市信義區忠孝東路5段"+'<br>'+'發生A2事故次數：901', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.050892, 121.482941], tooltip='地址：新北市三重區重新橋機車道路前0.0公尺'+'<br>'+'發生A2事故次數：900', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.05427, 121.496807], tooltip='地址：新北市三重區忠孝橋機車道路前0.0公尺'+'<br>'+'發生A2事故次數：764', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.029299, 121.561831], tooltip='地址：臺北市信義區吳興街 / 臺北市信義區吳興街'+'<br>'+'發生A2事故次數：692', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.006527, 121.467731], tooltip='地址：新北市板橋區浮洲橋機車專用道前0.0公尺'+'<br>'+'發生A2事故次數：689', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.081210, 121.548563], tooltip='地址：臺北市中山區北安路 / 臺北市中山區北安路'+'<br>'+'發生A2事故次數：654', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([25.036297, 121.452619], tooltip='地址：新北市新莊區中正路前0.0公尺'+'<br>'+'發生A2事故次數：649', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.184071, 120.612847], tooltip='地址：臺中市西屯區福恩里臺灣大道四段前0.0公尺'+'<br>'+'發生A2事故次數：644', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)
folium.Marker([24.901738, 121.720231], tooltip='地址：新北市坪林區北宜公路前0.0公尺'+'<br>'+'發生A2事故次數：623', icon=folium.Icon(color='blue', icon="fa-solid fa-location-pin")).add_to(m)

m.save('map.html')
