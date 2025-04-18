import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('processed_data.csv')

df['date_purchase'] = pd.to_datetime(df['date_purchase'])

# 可视化：按月销售额趋势
# 按月汇总销售额
monthly_sales = df.groupby(df['date_purchase'].dt.to_period('M'))['purchase_amount'].sum()

# 转换为 datetime 索引
monthly_sales.index = monthly_sales.index.to_timestamp()

# 可视化趋势
plt.figure(figsize=(10, 4))
monthly_sales.plot(marker='o')
plt.title('每月销售额趋势')
plt.xlabel('月份')
plt.ylabel('销售额（USD）')
plt.grid(True)
plt.show()
