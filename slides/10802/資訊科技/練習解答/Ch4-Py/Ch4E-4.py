def factorial(n):                  #函數名稱factorial及參數n
    if n < 0:                      #函數內部的程式碼--由此開始
        return '請輸入0或正整數'
    elif n <=1:
        return 1
    else:
        return n * factorial(n-1)  #函數內部的程式碼--到此結束
    
print (factorial(3))        #呼叫函數計算 3!
print (factorial(10))       #呼叫函數計算 10!
print (factorial(40))       #呼叫函數計算 40!
print (factorial(0)) 
print (factorial(-3))
