import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('processed_data.csv')

# 创建评分分组
df['rating_group'] = df['review_rating'].apply(lambda x: 'high' if x >= 4 else 'low')

print(df['rating_group'].value_counts())
print(df['rating_group'].describe())

# 可视化：高评分 vs 低评分 客户是否消费更多？
plt.figure(figsize=(6, 4))
sns.boxplot(x='rating_group', y='purchase_amount', data=df)
plt.title('高评分 vs 低评分客户的消费差异')
plt.xlabel('评分分组')
plt.ylabel('购买金额')
plt.show()

# 统计均值差异
grouped = df.groupby('rating_group')['purchase_amount'].mean()
print(grouped)

# 可视化：哪些商品更容易获得高评分？
item_rating = df.groupby('item_purchased')['review_rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(8, 4))
item_rating.plot(kind='bar')
plt.title('平均评分最高的商品 Top 10')
plt.ylabel('平均评分')
plt.xticks(rotation=45)
plt.show()

# 可视化：支付方式与客户满意度关联？
plt.figure(figsize=(6, 4))
sns.boxplot(x='payment_method', y='review_rating', data=df)
plt.title('不同支付方式的评分差异')
plt.xticks(rotation=45)
plt.show()

# 可视化：哪天买的人给的分高？
plt.figure(figsize=(8, 4))
sns.barplot(x='purchase_weekday', y='review_rating', data=df)
plt.title('星期几的平均评分（0=周一）')
plt.xlabel('星期几')
plt.ylabel('平均评分')
plt.show()
