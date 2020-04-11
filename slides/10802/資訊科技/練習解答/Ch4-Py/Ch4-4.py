num_array = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
x = num_array[0]        # x會變成 [1, 2, 3]
y = num_array[0][2]     # y會變成3
num_array[2][1] = -8    # num_array[2][1]由8變成-8
print(x)
print(y)
print(num_array[2][1])
