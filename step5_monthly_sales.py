import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('processed_data.csv')

# 确保日期列是datetime类型
df['date_purchase'] = pd.to_datetime(df['date_purchase'])

# 按月汇总销售额（保留年份信息）
monthly_sales = df.groupby(df['date_purchase'].dt.to_period('M'))['purchase_amount'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

# 创建带有月份名称的标签（格式：1月、2月...12月）
month_labels = [f"{date.month}月" for date in monthly_sales.index]

# 数据验证建议

# 检查日期范围
print(f"数据时间跨度：{df['date_purchase'].min()} 至 {df['date_purchase'].max()}")

# 验证金额有效性
print(f"异常值检测：\n{df['purchase_amount'].describe(percentiles=[0.01, 0.99])}")

# 检查月份完整性
print(f"缺失月份：{pd.date_range(start=monthly_sales.index.min(), end=monthly_sales.index.max(), freq='MS').difference(monthly_sales.index)}")

# 可视化趋势（优化版）
plt.figure(figsize=(12, 6))

# 绘制折线图
plt.plot(monthly_sales.index, monthly_sales.values, 
         marker='o', 
         linestyle='--', 
         color='#2c7fb8',
         markersize=8,
         linewidth=2)

# 设置X轴格式
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())  # 按月定位
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))  # 仅显示数字月份

# 自定义刻度标签
plt.xticks(monthly_sales.index,  # 确保每个数据点都有标签
           labels=month_labels,
           rotation=45,
           ha='right')

# 添加装饰元素
plt.title('月度销售额趋势（跨年度展示）', fontsize=14, pad=20)
plt.xlabel('月份', fontsize=12, labelpad=10)
plt.ylabel('销售额（USD）', fontsize=12, labelpad=10)
plt.grid(True, linestyle=':', alpha=0.7)

# 添加数据标签
for x, y in zip(monthly_sales.index, monthly_sales.values):
    plt.text(x, y, f'${y/1000:.1f}K', 
             ha='center', 
             va='bottom',
             fontsize=9)


# 自动调整布局
plt.tight_layout()
plt.show()

