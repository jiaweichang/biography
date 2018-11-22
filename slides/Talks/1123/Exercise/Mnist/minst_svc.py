from sklearn.datasets import load_digits  # 載入預設手寫資料庫
from sklearn.model_selection import train_test_split  # 切割資料為訓練與測試集  
from sklearn.preprocessing import StandardScaler  # 標準化
from sklearn.svm import LinearSVC  
from sklearn.metrics import classification_report  # 預測結果的分析工具  
import matplotlib.pyplot as plt

# 載入 `digits` --- Step 1. 圖像取得
digits = load_digits()

# 設定圖形的大小（寬, 高）
fig = plt.figure(figsize=(4, 2))

# 調整子圖形 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# 把前 8 個手寫數字顯示在子圖形
for i in range(10):
    # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
    ax = fig.add_subplot(2, 5, i + 1, xticks = [], yticks = [])
    # 顯示圖形，色彩選擇灰階
    ax.imshow(digits.images[i], cmap = plt.cm.binary) # Step 2. 預處理
    # 在左下角標示目標值
    ax.text(0, 9, str(digits.target[i]))

# 顯示圖形
plt.show();
  
# 分割數據
X_train, X_test, Y_train, Y_test = train_test_split(digits.data, digits.target, test_size=0.25)  
  
ss = StandardScaler() #標準化方法 Step 2. 預處理 (原始值−均值)/標準差
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)
  
lsvc = LinearSVC()
lsvc.fit(X_train, Y_train) # Step 3. & 4. 特徵提取與檢測  
  
Y_predict = lsvc.predict(X_test) # Step 5. 分類
  
print (classification_report(Y_test, Y_predict, target_names=digits.target_names.astype(str))) # Step 5. 驗證