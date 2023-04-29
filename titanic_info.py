import pandas as pd
from lib.utils import show_df_info

data_path = './data'
df = pd.read_csv(f'{data_path}/titanic.csv')
show_df_info(df)
