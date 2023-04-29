import pandas as pd
from lib.utils import show_df_info
from sklearn.preprocessing import OneHotEncoder

data_path = './data'
df = pd.read_csv(f'{data_path}/titanic.csv')

enc = OneHotEncoder()
transformed = enc.fit_transform(df[['Sex']])
df['Sex_ohe'] = transformed.toarray()[:, 1]
df.to_csv(f'{data_path}/titanic.csv', index=True)

