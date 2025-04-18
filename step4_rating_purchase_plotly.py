
import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_data.csv')

df['rating_group'] = df['review_rating'].apply(lambda x: '高评分（≥4）' if x >=4 else '低评分（<4）')

fig = px.box(df, x='rating_group', y='purchase_amount', 
             color='rating_group', points="all",
             title="<b>交互式消费金额分析</b><br><sup>鼠标悬停查看详细信息</sup>")
fig.update_traces(quartilemethod="exclusive") 
fig.show()