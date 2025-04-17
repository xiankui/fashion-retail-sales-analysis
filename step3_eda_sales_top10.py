import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

# 数据可视化 - 热门商品 Top 10
plt.figure(figsize=(8, 4))
df['item_purchased'].value_counts().head(10).plot(kind='bar')
plt.title('最受欢迎的商品 Top 10')
plt.ylabel('购买次数')
plt.xticks(rotation=45)
plt.show()
