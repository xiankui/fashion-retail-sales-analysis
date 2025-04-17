import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('processed_data.csv')

# 创建1行2列的画布
plt.figure(figsize=(18, 4))

# 数据可视化 - 月份分布
plt.subplot(1, 2, 1)
sns.countplot(x='purchase_month', data=df)
plt.title('每月购买量分布')
plt.xlabel('月份')
plt.ylabel('购买量')

# 数据可视化 - 星期几分布
plt.subplot(1, 2, 2)
sns.countplot(x='purchase_weekday', data=df)
plt.title('一周购买习惯（0=周一）')
plt.xlabel('星期几')
plt.ylabel('购买量')

# 合并视图
plt.tight_layout()
plt.show()