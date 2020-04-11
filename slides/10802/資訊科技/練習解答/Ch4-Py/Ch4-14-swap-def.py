def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp            #不必return
num_visitors = [70, 10, 14, 7, 25, 30, 50] #索引0~6代表星期日到六
print(num_visitors)
swap(num_visitors, 0, 6)   #把星期日及星期六的人數交換
print(num_visitors)
