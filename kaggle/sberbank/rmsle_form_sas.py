## RMSLE from SAS
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_squared_log_error, r2_score

lasso_result = pd.read_csv("./data/lasso_result.csv")
l_result = lasso_result[lasso_result._ROLE_ == 'VALIDATE'][['price_doc', 'predict']]
l_result['predicted_price'] = np.exp(l_result.predict)

"""
price_doc	predict		predicted_price
13100000	16.194		10787184.520
5300000		15.594		5923265.639
5200000		15.498		5381071.318
"""


print("RMSLE: ", np.sqrt(mean_squared_log_error(abs(l_result.predict),l_result.price_doc)))