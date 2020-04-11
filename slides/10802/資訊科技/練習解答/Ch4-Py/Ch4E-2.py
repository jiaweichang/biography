grades = [[100, 20, 85],[95,99,75],[89,73,92]]
names = ['嘉明', '小美', '阿雄']

for i in range(3):
    sum = 0
    for j in range(3):
        sum += grades[i][j]
    print(names[i], '總分為', sum, '分')
