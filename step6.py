from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('processed_data.csv')

df['date_purchase'] = pd.to_datetime(df['date_purchase'])

## 1. 构建数据集：时间序列建模准备

# 准备数据（用月份作为时间索引）
monthly_sales = df.groupby(df['date_purchase'].dt.to_period('M'))['purchase_amount'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
monthly_sales = monthly_sales.sort_index()

# 构建模型输入
X = np.arange(len(monthly_sales)).reshape(-1, 1)  # 时间步：0, 1, 2, ...
y = monthly_sales.values

## 2. 拆分训练集 & 测试集（时间序列不可随机划分）

# 简单 80% 训练，20% 测试
split_idx = int(len(X) * 0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

## 3. 训练线性回归模型

model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 计算 RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"测试集 RMSE：{rmse:.2f}")

## 4. 可视化真实 vs 预测值

# 拼接时间索引
dates = monthly_sales.index
train_dates = dates[:split_idx]
test_dates = dates[split_idx:]

plt.figure(figsize=(10, 4))
plt.plot(train_dates, y_train, label='训练集实际值')
plt.plot(test_dates, y_test, label='测试集实际值')
plt.plot(test_dates, y_pred, label='预测值', linestyle='--')
plt.title('线性趋势预测：月度销售额')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.legend()
plt.grid(True)
plt.show()
