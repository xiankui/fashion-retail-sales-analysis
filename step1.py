# 数据清洗 - 清理异常值与空值

import pandas as pd

# 读取数据
df = pd.read_csv('Fashion_Retail_Sales.csv')

# 快速预览
print(df.head())
print(df.info())

### 清洗步骤

# 1. 重命名列（去除空格，标准化）
df.columns = (
    df.columns.str.strip()  # 去除两端空格
    .str.replace(r'\s*\(.*?\)$', '', regex=True)  # 移除末尾括号及其内容
    .str.replace(' ', '_')  # 空格转下划线
    .str.lower()  # 转为小写
)

# 2. 转换日期格式 05-02-2023 => 2023-02-05, errors='coerce' => 将无法转换的日期转换为NaT
df['date_purchase'] = pd.to_datetime(df['date_purchase'], format='%d-%m-%Y', errors='coerce')
# df['purchase_amount'] > 0，避免类型比较报错
df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")

# 3. 检查缺失值
print(df.isnull().sum())

# 4. 删除缺失严重或格式错误的行
df = df.dropna()

# 5. 去除重复项
df = df.drop_duplicates()

# 6. 检查购买金额是否为正数 (删除 purchase_amount 非正数的行（包括 0、负数、缺失值 NaN）)
df = df[df['purchase_amount'] > 0]

print(df.info())