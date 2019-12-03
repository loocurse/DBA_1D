import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from initialise_dataset import create_coy_dataset, china_stocks_large, full_data_coy
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from time_series_analysis import predict_volatility


error_1, error_2 = (list(), list())


for idx, company in enumerate(full_data_coy):
    try:
        x,y = predict_volatility(company,print_error=True)
        error_1.append(x)
        error_2.append(y)
    except:
        error_1.append(np.NaN)
        error_2.append(np.NaN)


mse = pd.DataFrame([full_data_coy,error_1,error_2])