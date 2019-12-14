import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initialise_dataset import china_stocks_large, create_coy_dataset, full_data_coy

correlation_df = pd.DataFrame(index=china_stocks_large.columns)

def find_corr(df):
    corr = df.corr()
    return corr['rolling_std']

# Get correlations of each company
for i in range(20):
    create_coy_dataset(full_data_coy[i],export_to_csv=True)
    # df = create_coy_dataset(full_data_coy[i])
    # correlation_df[str(full_data_coy[i])] = find_corr(df)

correlation_df.to_csv('correlation_20.csv')

test_df = pd.read_csv('coy_3544_edited.csv')
test_df.head()
corr = test_df.corr()

# Find the rolling pct difference between each value and
difference = pd.DataFrame()
for index, col in test_df.iteritems():
    try:
        change = col.pct_change()
        difference[col.name] = change
    except:
        print(f'Error on {col.name}')

difference.to_csv('difference.csv')

difference_edited = pd.read_csv('difference.csv')
difference_edited.corr().to_csv('difference_corr.csv')