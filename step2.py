import pandas as pd

# 读取数据
df = pd.read_csv('Fashion_Retail_Sales.csv')

### 数据清洗 - 清理异常值与空值 清洗步骤

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
# print(df.isnull().sum())

# 4. 删除缺失严重或格式错误的行
df = df.dropna()

# 5. 去除重复项
df = df.drop_duplicates()

# 6. 检查购买金额是否为正数 (删除 purchase_amount 非正数的行（包括 0、负数、缺失值 NaN）)
df = df[df['purchase_amount'] > 0]


### 数据预处理 - 特征工程

## 步骤一： 标准化类别数据

# 查看所有对象类型字段（通常是分类变量）
print(df.select_dtypes(include='object').nunique())

# 使用 Label Encoding（适合无序类别）
from sklearn.preprocessing import LabelEncoder

label_cols = ['item_purchased', 'payment_method']
label_encoders = {}

# 对每个列进行编码，保存编码器
# 为什么要进行编码？
# 因为分类变量的值可能会影响模型的性能，因此需要进行编码
for col in label_cols:
    le = LabelEncoder()
    df[col + '_encoded'] = le.fit_transform(df[col])
    label_encoders[col] = le  # 保存编码器以便后续使用/反编码

# 打印编码后的类别，以便检查，看看有哪些类别，有多少个，有哪些值
print(label_encoders['item_purchased'].classes_)

## 步骤二： 创建新特征 - 日期拆解
df['purchase_month'] = df['date_purchase'].dt.month
df['purchase_weekday'] = df['date_purchase'].dt.dayofweek  # 0=Monday
df['purchase_day'] = df['date_purchase'].dt.day

## 步骤三：构造业务特征示例（示范）

# 客户平均消费金额，保留两位小数
df['avg_spend_per_customer'] = df.groupby('customer_reference_id')['purchase_amount'].transform('mean').round(2)

# 打印处理后的数据
print(df.head())

# 保存处理后的数据
df.to_csv('processed_data.csv', index=False)