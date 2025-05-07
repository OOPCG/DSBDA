import pandas as pd
df = pd.read_csv(&quot;dataset.csv&quot;)
print(df)
print(df.head(15))
df.isnull().sum()
print(df.describe())
df.dtypes
df.dropna(axis=1)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)
print(df[&#39;race/ethnicity&#39;].value_counts())
df_Lunch = pd.get_dummies(df[&#39;lunch&#39;])
df_new = pd.concat([df, df_Lunch], axis=1)
print(df_new)
