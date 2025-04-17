import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据加载
df = pd.read_csv('processed_data.csv')

# 字体兼容性
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set(style="whitegrid")

# 创建1行3列的画布
plt.figure(figsize=(18, 5))

# ---------------------------
# 子图1：评分分布柱状图
# ---------------------------
plt.subplot(1, 3, 1)
sns.countplot(  # 更适合离散型评分数据
    data=df,
    x='review_rating',
    hue='review_rating',
    palette='viridis',
    edgecolor='black',
    legend=False, # 隐藏图例
    dodge=False, # 不分离
)
plt.title('评分分布柱状图')
plt.xlabel('顾客评分（1-5分）')
plt.ylabel('评价数量')
plt.xticks(ticks=[0,1,2,3,4], labels=['1','2','3','4','5'])  # 明确显示所有评分

# ---------------------------
# 子图2：评分分布箱线图（需特殊处理）
# ---------------------------
plt.subplot(1, 3, 2)
sns.boxplot(  # 展示评分分布特征
    data=df,
    x='review_rating',
    color='skyblue',
    width=0.6,
    showmeans=True,  # 显示均值点
    meanprops={"marker":"o","markerfacecolor":"red"} 
)
plt.title('评分分布箱线图')
plt.xlabel('顾客评分（1-5分）')
plt.xlim(-0.5, 4.5)  # 防止边缘留白

# ---------------------------
# 子图3：累积比例分布
# ---------------------------
plt.subplot(1, 3, 3)
sns.ecdfplot(
    data=df,
    x='review_rating',
    color='purple',
    stat='proportion',
    complementary=False,  # 正向累积
    lw=2
)
plt.title('累积评分分布')
plt.xlabel('顾客评分（1-5分）')
plt.ylabel('累积比例')
plt.xticks([1,2,3,4,5])  # 强制显示所有刻度

# 统一展示
plt.tight_layout()
plt.show()

print(df['review_rating'].describe())