def sum(n):                  #函數名稱sum及參數n
    if n <= 1:               #函數內部的程式碼--由此開始
        return 1
    else:
        return n + sum(n-1)  #函數內部的程式碼--到此結束
print (sum(3))               #呼叫函數計算 3+2+1
print (sum(10))              #呼叫函數計算 10+9+8+...+1
print (sum(40))              #呼叫函數計算 40+39+38+...+1
