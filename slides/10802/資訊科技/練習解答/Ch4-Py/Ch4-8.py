animals_2d = [
['長頸鹿', '獅子', '兔子'],
['樹葉', '肉', '紅蘿蔔']
]
for i in range(2):       #外層控制animals_2d第i個元素(陣列)
    for j in range(3):   #內層控制animals_2d第i個元素(陣列)的第j個元素
        print(animals_2d[i][j])
