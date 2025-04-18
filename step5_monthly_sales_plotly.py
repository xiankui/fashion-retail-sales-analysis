import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_data.csv')

df['date_purchase'] = pd.to_datetime(df['date_purchase'])

# 按月汇总销售额
monthly_sales = df.groupby(df['date_purchase'].dt.to_period('M'))['purchase_amount'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

fig = px.line(monthly_sales, 
              x=monthly_sales.index, 
              y='purchase_amount',
              title='<b>交互式销售趋势</b>',
              markers=True)

fig.update_layout(hovermode="x unified")
fig.show()
