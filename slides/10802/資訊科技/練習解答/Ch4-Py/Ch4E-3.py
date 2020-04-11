grades = [40, 80, 75, 20, 96, 69, 50]
lower_60 = 0
higher_90 = 0
for i in range(7):
    if grades[i] > 90:
        higher_90 = higher_90 + 1
    elif grades[i] < 60:
        lower_60 = lower_60 + 1
print('<60分: ', lower_60, '個')
print('>90分: ', higher_90, '個')
