from datascience import *
# %matplotlib inline
import matplotlib.pyplot as plots

plots.style.use('fivethirtyeight')
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

###########################read the file###
companies = Table.read_table('China_A_200101_201906.csv')

#######################find industry names###
industry_names = companies.group('industry_group').column('industry_group')
print(industry_names)


###############group certain industry by month#####################
def group_industry_bymonth(industry):
    industry_ror = companies.select('industry_group', 'total_ror', 'py_month_end').where('industry_group', industry)
    return industry_ror.drop('industry_group').group('py_month_end', np.nanmean).sort('py_month_end')


# group_industry_bymonth('WHOLESALE')


################keyin one industry and return an array of its rolling std###########
def industry_with_rolling(industry):
    print('Industry name:' + industry)
    ror = group_industry_bymonth(industry).column('total_ror nanmean')
    rolling_std = make_array()
    for i in range(len(ror)):
        indices = np.arange(i, i + 11)
        if i >= len(ror) - 11:
            indices = np.arange(i, len(ror))
            rolling_std = np.append(rolling_std, np.nanstd(np.take(ror, indices)))
        else:
            rolling_std = np.append(rolling_std, np.nanstd(np.take(ror, indices)))
    #  industry_with_rollingstd=group_industry_bymonth(industry).with_column('rolling_std', rolling_std)
    print('rolling std')
    return rolling_std


# print(industry_with_rolling('SOFTWARE'))

####################find array of rolling std by month which will give us std for the whole economy#######
group_month = companies.select('py_month_end', 'total_ror').group('py_month_end', np.nanmean)
month_ror = group_month.column('total_ror nanmean')
economy_rolling_std = make_array()
for i in range(len(month_ror)):
    indices = np.arange(i, i + 11)
    if i >= len(month_ror) - 11:
        indices = np.arange(i, len(month_ror))
        economy_rolling_std = np.append(economy_rolling_std, np.nanstd(np.take(month_ror, indices)))
    else:
        economy_rolling_std = np.append(economy_rolling_std, np.nanstd(np.take(month_ror, indices)))
# print(rolling_std)
