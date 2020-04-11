n = 3                      # 求n!
product = 1                # 先設乘積變數product為1
for i in range(n):         # i在每回合中分別為0,1,2,...,n-1
    product = (i+1) * product  # i+1在每回合中分別為1,2,3,...,n
print(product)
