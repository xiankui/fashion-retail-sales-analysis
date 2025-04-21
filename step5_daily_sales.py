import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

# 按日聚合
daily_sales = df.groupby('date_purchase')['purchase_amount'].sum()

plt.figure(figsize=(10, 4))
daily_sales.plot()
plt.title('每日销售额变化趋势')
plt.xlabel('日期')
plt.ylabel('销售额')
plt.show()


# 添加7日滚动平均
rolling_avg = daily_sales.rolling(window=7).mean()

plt.figure(figsize=(10, 4))
plt.plot(daily_sales, label='每日销售额', alpha=0.5)
plt.plot(rolling_avg, label='7日滚动平均', color='red')
plt.title('每日销售趋势 + 滚动平均')
plt.legend()
plt.show()

# 销售高峰识别（Top 10 高销售日）
top_days = daily_sales.sort_values(ascending=False).head(10)
print("销售额最高的10天：")
print(top_days)
