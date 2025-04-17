# 探索性数据分析 - 购买金额
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据加载
df = pd.read_csv('processed_data.csv')

# 创建1行3列的画布
plt.figure(figsize=(18, 5))

# ---------------------------
# 子图1：直方图+KDE
# ---------------------------
plt.subplot(1, 3, 1) # 1行3列的第一个子图
sns.histplot(
    data=df,
    x='purchase_amount',
    bins=30,
    kde=True,
    color='royalblue',
    edgecolor='white'
)
plt.title('金额分布直方图')
plt.xlabel('购买金额（USD）')
plt.ylabel('频数')

# ---------------------------
# 子图2：箱线图
# ---------------------------
plt.subplot(1, 3, 2)
sns.boxplot(
    data=df,
    x='purchase_amount',
    color='lightgreen',
    width=0.4
)
plt.title('金额分布箱线图')
plt.xlabel('购买金额（USD）')

# ---------------------------
# 子图3：累积分布图
# ---------------------------
plt.subplot(1, 3, 3)
sns.ecdfplot(
    data=df,
    x='purchase_amount',
    color='crimson',
    stat='proportion' 
)
plt.title('累积分布曲线')
plt.xlabel('购买金额（USD）')
plt.ylabel('累积比例')

# 统一展示
plt.tight_layout()
plt.show()