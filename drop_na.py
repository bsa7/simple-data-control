import pandas as pd
from lib.utils import show_df_info

data_path = './data'
df = pd.read_csv(f'{data_path}/titanic.csv')
# show_df_info(df)

filter = df['Age'].isna()
show_df_info(df.loc[filter])
mean = round(df['Age'].mean(), 1)
df.loc[filter, 'Age'] = df.loc[filter, 'Age'].fillna(mean)

df.to_csv(f'{data_path}/titanic.csv', index=True)

