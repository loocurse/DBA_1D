from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initialise_dataset import create_coy_dataset, china_stocks_large, full_data_coy, create_list_of_coys
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from time_series_analysis import predict_volatility


error_1, error_2 = (list(), list())


# for idx, company in enumerate(full_data_coy):
#     try:
#         error_arima, error_naive = predict_volatility(company,print_error=True)
#         error_1.append(error_arima)
#         error_2.append(error_naive)
#     except:
#         error_1.append(np.NaN)
#         error_2.append(np.NaN)


# mse = pd.DataFrame([full_data_coy,error_1,error_2])

### To test if discount in number of data == inaccuracy in data

a = defaultdict(int)

for counts in [222]:
    group_of_coys = create_list_of_coys(counts)
    errors_of_coys = list()
    for company in group_of_coys[:10]:
        print(counts, company)
        try:
            error_arima, error_naive = predict_volatility(company, print_error=True)
            errors_of_coys.append(np.mean(error_arima))
        except:
            pass
    a[counts] = np.mean(errors_of_coys)
