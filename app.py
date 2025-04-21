import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="时尚零售数据分析", layout="wide")
st.title("👗 Fashion Retail Sales 分析仪表盘")

@st.cache_data
def load_data():
    df = pd.read_csv("Fashion_Retail_Sales.csv")
    df.rename(columns={
        'Customer Reference ID': 'customer_id',
        'Item Purchased': 'item_purchased',
        'Purchase Amount (USD)': 'purchase_amount',
        'Date Purchase': 'date_purchase',
        'Review Rating': 'review_rating',
        'Payment Method': 'payment_method'
    }, inplace=True)
    df['date_purchase'] = pd.to_datetime(df['date_purchase'], format='%d-%m-%Y')
    df['review_rating'] = pd.to_numeric(df['review_rating'], errors='coerce')
    df = df[(df['purchase_amount'] > 0) & (df['purchase_amount'] < 10000)]
    df.dropna(inplace=True)
    return df

# 加载数据
df = load_data()

# 折叠部分统计信息
with st.expander("📊 数据预览"):
    st.dataframe(df.head())
    st.markdown(f"共计 {len(df)} 条记录")

# 商品选择器
item_options = st.multiselect("选择商品查看销售趋势：", options=df['item_purchased'].unique(), default=df['item_purchased'].unique()[:3])

# 销售趋势图
st.subheader("📈 销售趋势图")
filtered_df = df[df['item_purchased'].isin(item_options)]
daily_sales = filtered_df.groupby(['date_purchase', 'item_purchased'])['purchase_amount'].sum().reset_index()

fig, ax = plt.subplots()
sns.lineplot(data=daily_sales, x='date_purchase', y='purchase_amount', hue='item_purchased', ax=ax)
ax.set_title('每日销售额趋势')
st.pyplot(fig)

# 评分与消费关系
st.subheader("⭐ 高评分 vs 低评分 消费差异")
df['rating_group'] = df['review_rating'].apply(lambda x: 'High (>=4)' if x >= 4 else 'Low (<4)')
fig2, ax2 = plt.subplots()
sns.boxplot(data=df, x='rating_group', y='purchase_amount', ax=ax2)
ax2.set_title("评分分组消费金额对比")
st.pyplot(fig2)

# 月销售额预测
st.subheader("📉 简单线性预测：未来销售趋势")
monthly_sales = df.groupby(df['date_purchase'].dt.to_period('M'))['purchase_amount'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.arange(len(monthly_sales)).reshape(-1, 1)
y = monthly_sales.values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

fig3, ax3 = plt.subplots()
ax3.plot(monthly_sales.index, y, label='实际值')
ax3.plot(monthly_sales.index, y_pred, '--', label='预测趋势')
ax3.set_title('月度销售预测（线性回归）')
ax3.legend()
st.pyplot(fig3)
