num_visitors = [
[50, 10, 14, 7, 25, 30, 70],
[30, 24, 14, 9, 87, 63, 25],
[100, 52, 82, 89, 36, 78, 22] 
]
day_names = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
for week_index in range(3):              # 有3個星期的資料，因此是range(3)
    #注意縮排，以下這個print()屬於外層迴圈
    print('第', week_index + 1, '個星期')  
    for day_index in range(7):           # 一星期有7天，因此是range(7)
        #注意縮排，以下這個print()屬於內層迴圈
        print(day_names[day_index], num_visitors[week_index][day_index], '人')
