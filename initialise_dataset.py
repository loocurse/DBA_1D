import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import nanstd

china_stocks = pd.read_csv('China_A_200101_201906.csv')

# Convert dtypes
china_stocks['cxrf'] = china_stocks.cxrf.astype('category')
china_stocks['economic_sector_group'] = china_stocks.economic_sector_group.astype('category')
china_stocks['industry_group'] = china_stocks.industry_group.astype('category')
china_stocks['market'] = china_stocks.market.astype('category')
china_stocks['returns'] = china_stocks['total_ror'] - 1

# Remove irrelevant columns
# for idx, col in china_stocks.iteritems(): # Find columns which are irrelevant
#
#     print(f'Column:{idx}')
#     print(f'Unique entries {col.nunique()}')
#     print(f'Non-NaN entries: {((266518 - col.isna().sum())/266518) * 100}',end='\n\n')

china_stocks = china_stocks.drop(columns=['a_p', 'calf', 'a_p_cwcnorm', 'accr_cwcnorm', 'bps_cwcnorm',
                                          'calf_cwcnorm', 'cflow_cwcnorm', 'rosa_cwcnorm', 'erv6', 'erv6_cwcnorm',
                                          'market', 'total_ror'])

counts_of_companies = china_stocks['cxrf'].value_counts()
full_data_coy = counts_of_companies[counts_of_companies == counts_of_companies.max()].index.tolist()
china_stocks_large = china_stocks.loc[china_stocks['cxrf'].isin(full_data_coy)]


# Creating dataset for one company
def create_coy_dataset(company_number, export_to_csv=False):
    '''Takes in a company's number and returns a dataframe with the company's information
    sorted according to date, with a rolling standard deviation of 12 months and its difference'''
    output = china_stocks_large.loc[china_stocks_large.cxrf == company_number]
    output = output.sort_values('py_month_end')
    returns = output.loc[:, 'returns']
    rolling = returns.rolling(12, min_periods=5).apply(nanstd, raw=False)
    differences = rolling.diff()

    output['rolling_std'] = rolling
    output['std_diff'] = differences
    if export_to_csv:
        output.to_csv(f'coy_{company_number}.csv', index=False)
    return output
