import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv('processed_data.csv')

# 创建评分分组
df['rating_group'] = df['review_rating'].apply(lambda x: '高评分（≥4）' if x >=4 else '低评分（<4）')

# 创建复合图表
plt.figure(figsize=(10, 6))
ax = plt.gca()

# ---------------------------
# 主图：箱线图+散点图
# ---------------------------
# 箱线图基础
sns.boxplot(
    x='rating_group',
    y='purchase_amount',
    data=df,
    palette=['#2ecc71', '#e74c3c'],  # 定制颜色
    width=0.4,
    showmeans=True,  # 显示均值标记
    meanprops={"marker":"D", "markerfacecolor":"gold", "markersize":"10"}  # 金色菱形
)

# 叠加散点图显示分布密度
sns.stripplot(
    x='rating_group',
    y='purchase_amount',
    data=df,
    color='black',
    alpha=0.2,
    jitter=0.2,
    size=3
)

# ---------------------------
# 统计标注
# ---------------------------
# 计算各组统计量
high = df[df['rating_group']=='高评分（≥4）']['purchase_amount']
low = df[df['rating_group']=='低评分（<4）']['purchase_amount']

# T检验
t_stat, p_value = stats.ttest_ind(high, low)

# 添加统计标注
plt.text(0.5, max(df['purchase_amount'])*0.95, 
         f"p-value = {p_value:.3f}\n(独立样本t检验)",
         ha='center',
         bbox=dict(facecolor='white', alpha=0.8))

# ---------------------------
# 样式优化
# ---------------------------
plt.title('高/低评分客户消费金额差异分析', fontsize=14, pad=20)
plt.xlabel('评分分组', fontsize=12, labelpad=10)
plt.ylabel('购买金额（USD）', fontsize=12, labelpad=10)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()
plt.show()

# 输出详细统计
print(f'''
=== 分组统计报告 ===
高评分组（{len(high)} 个样本）：
  均值：${high.mean():.2f}
  中位数：${high.median():.2f}
  标准差：${high.std():.2f}

低评分组（{len(low)} 个样本）：
  均值：${low.mean():.2f}
  中位数：${low.median():.2f}
  标准差：${low.std():.2f}

统计显著性：
  t-statistic = {t_stat:.2f}
  p-value = {p_value:.3f}
''')
