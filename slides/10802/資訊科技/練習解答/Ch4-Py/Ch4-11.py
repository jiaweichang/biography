num_visitors = [50, 10, 14, 7, 25, 30, 70]
day_names = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
for day_index in range(7):
    if num_visitors[day_index] > 35:
        print(day_names[day_index], ' 人數爆棚！')
    else:
        print(day_names[day_index], ' 需要繼續加油...')
