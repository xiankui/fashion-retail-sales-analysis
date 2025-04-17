import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文/字体兼容性
plt.rcParams['font.family'] = 'SimHei'
sns.set(style="whitegrid")

# 读取数据 - 预处理后的数据
df = pd.read_csv('processed_data.csv')

# 数据探索
print(f"总销售金额：${df['purchase_amount'].sum():,.2f}")

# Seaborn是基于matplotlib的高级封装库，他们具有隐式协作关系，可以使用Seaborn的函数来创建更加复杂的图形，包括直方图，散点图，箱线图等
# 其协作方式如下
# plt.figure()              # matplotlib创建画布
# sns.histplot(...)         # seaborn在matplotlib画布上绘图
# plt.xxx()                 # 用matplotlib方法进一步修饰
# plt.show()                # 用matplotlib最终渲染

# 数据可视化 - 消费金额分布
plt.figure(figsize=(8, 4)) # 初始化画布，设置图像尺寸为8x4英寸
sns.histplot(df['purchase_amount'], kde=True, bins=30) # 绘制直方图，并添加密度曲线，直方图的柱子数量为30
plt.title('消费金额分布')
plt.xlabel('购买金额（USD）')
plt.ylabel('频数')
plt.show()

# 数据可视化 - 顾客评分分布
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['review_rating'])
plt.title('顾客评分分布（箱线图）')
plt.xlabel('评分')
plt.show()

print(df['review_rating'].describe())

# 数据可视化 - 热门商品 Top 10
plt.figure(figsize=(8, 4))
df['item_purchased'].value_counts().head(10).plot(kind='bar')
plt.title('最受欢迎的商品 Top 10')
plt.ylabel('购买次数')
plt.xticks(rotation=45)
plt.show()

# 数据可视化 - 支付方式分布
plt.figure(figsize=(6, 4))
df['payment_method'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('支付方式占比')
plt.ylabel('')
plt.show()

# 数据可视化 - 月份分布
plt.figure(figsize=(8, 4))
sns.countplot(x='purchase_month', data=df)
plt.title('每月购买量分布')
plt.xlabel('月份')
plt.ylabel('购买量')
plt.show()

# 数据可视化 - 星期几分布
plt.figure(figsize=(8, 4))
sns.countplot(x='purchase_weekday', data=df)
plt.title('一周购买习惯（0=周一）')
plt.xlabel('星期几')
plt.ylabel('购买量')
plt.show()
