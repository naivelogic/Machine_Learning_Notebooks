# Linear Regression
# https://alstatr.blogspot.com/2015/08/r-python-and-sas-getting-started-with.html

"""
Suppose we want to fit the model to fthe following data Average Heights and WEights for American Women, where _weight_ is the response (y) and _height_ is the predictor (x). Therefore our model is:

        weight = β0 + β1(height) + ε

There are two modules that have implementation of linear regerssion modelling, one is in `sklearn` and the other is in `statmodels`. We will use `sklearn`.
"""

from sklearn import linear_model
from pandas import DataFrame

dat = {'height': [58, 59, 60, 61, 62, 63, 64, 65,
                  66, 67, 68, 69, 70, 71, 72],
       'weight': [115, 117, 120, 123, 126, 129, 132,
                  135, 139, 142, 146, 150, 154, 159, 164]}

women = DataFrame(data = dat, columns = ['height', 'weight'])
model = linear_model.LinearRegression(fit_intercept= True)
height = women.height.values.reshape(len(women), 1)
weight = women.weight.values.reshape(len(women), 1)
fit = model.fit(height, weight)
print("Intercept: %.4f, Height: %.4f" % (fit.intercept_, fit.coef_))

# Output
"""
Intercept: -87.5167, Height: 3.4500
Above output is the estimate of the parameters, to obtain the predicted values and plot these along with the data points

"""

__author__ = 'al-ahmadgaidasaad'

from sklearn import linear_model
from pandas import read_csv, DataFrame
import numpy as np
from scipy.stats import t
import seaborn
import matplotlib.pylab as plt

class linear_regression(object):
    """ Fit linear model to the data.
    Parameters
    ----------
    x : numpy array or sparse matrix of shape [n_samples,n_features]
        Independent variable defined in the column of data argument below.
    y : numpy array of shape [n_samples, n_targets]
        Dependent variable defined in the column of the data argument below.
    data: pandas DataFrame or str instance (local path/directory of the data)
        Data frame with columns x and y defined above.
    intercept: boolean, default False
        Toggle intercept of the model.
    Examples
    --------
    >>> model = linear_regression('height', 'weight', data = 'women.csv')
    >>> print model
    >>> model = linear_regression('height', 'weight', data = 'women.csv', intercept = True)
    >>> print model
    """

    def __init__(self, x, y, data, intercept = False):
        self.intercept = intercept
        self.x = str(x)
        self.y = str(y)

        if isinstance(data, str):
            self.data = read_csv(data)
        else:
            if isinstance(data, DataFrame):
                self.data = data
            else:
                raise TypeError('%s should be a pandas.DataFrame instance' % data)

        self.indv = np.array(self.data.loc[:, x]).reshape((len(self.data), 1))
        self.depv = np.array(self.data.loc[:, y]).reshape((len(self.data), 1))
        _regr_ = linear_model.LinearRegression(fit_intercept = self.intercept)
        self.fit = _regr_.fit(self.indv, self.depv)

    def __str__(self):
        if self.intercept is True:
            _model_ = 'Model:\n' \
                    '\t(%s) = %6.3f + %6.3f * (%s) + error' % (self.y, self.fit.intercept_, self.fit.coef_, self.x)
            _summary_ = 'Summary:\n\t\t\t\tEstimates\n' \
                      '\t(Intercept)\t %8.3f\n' \
                      '\t%s\t\t %8.3f' % (self.fit.intercept_, self.x, self.fit.coef_)
        else:
            _model_ = 'Model:\n' \
                      '\t(%s) = %6.3f * (%s) + error' % (self.y, self.fit.coef_, self.x)
            _summary_ = 'Summary:\n\t\t\tEstimates\n' \
                        '\t%s\t\t %8.3f' % (self.x, self.fit.coef_)
        return '%s\n\n%s' % (_model_, _summary_)

    def predict(self, x = None, plot = False, conf_level = 0.95, save_fig = False, filename = 'figure', fig_format = '.pdf'):
        """ Predict linear model given x.
        Parameters
        ----------
        x : numpy array or sparse matrix of shape [n_samples,n_features], default None
            Independent variable, if set to None, the original X (predictor) variable
            of the model will be used.
        plot : boolean, default False
            Toggle plot of the data points along with its predicted values and confidence interval.
        conf_level: float between 0 and 1, default 0.95
            Confidence level of the confidence interval in plot. Enabled if plot is True.
        save_fig: boolean, default False
            Toggle to save plot.
        filename: str, default 'figure'
            Name of the file if save_fig is True.
        fig_format: str, default 'pdf'
            Format of the figure if save_fig is True, choices are: 'png', 'ps', 'pdf', and 'svg'.
        Examples
        --------
        >>> from pandas import DataFrame
        >>> from numpy import random.normal
        >>> df = {'x': random.normal(50, 25, 5), 'y': random.normal(50, 25, 5)}
        >>> model = linear_regression('height', 'weight', data = 'women.csv')
        >>> model.predict()
        Returns
        --------
        _res_df_: pandas DataFrame of shape [n_samples,n_features]
            A DataFrame of columns (features) 'Predicted', 'Lower' (Confidence Limit), 'Upper' (Confidence Limit)
        See Also
        --------
        sklearn.linear_model.LinearRegression.predict
            Predict using the linear model
        """
        if x is not None and isinstance(x, np.ndarray) and len(x.shape) is 1:
            _x_ = x.reshape((len(x), 1))
        elif x is not None and isinstance(x, np.ndarray) and len(x.shape) is 2 and x.shape[0] is len(x):
            _x_ = x
        elif x is None:
            _x_ = self.indv
        else:
            raise TypeError('%s should be one dimensional numpy array' % x)

        _yhati_ = self.fit.predict(self.indv)
        _yhat_ = self.fit.predict(_x_)
        _ci_ = self.yhat_ci(_yhat_, _yhati_, _x_, alpha = 1 - conf_level)
        
        if plot is True:
            plt.plot(self.indv, self.depv, 'o', color = 'red', label = 'Data Points', markersize = 8)
            plt.plot(_x_, _yhat_, '--', color = 'black', label = 'Fitted Values')
            plt.plot(_x_, _ci_[:,0], '-', color = 'orange', label = '%.1f Confidence Interval' % (conf_level * 100))
            plt.plot(_x_, _ci_[:,1], '-', color = 'orange')
            plt.legend(loc = 'lower right')
            if save_fig is True:
                plt.savefig(filename + '.' + fig_format)
            else:
                plt.show

        _res_mat_ = np.column_stack((_yhat_, _ci_))
        _res_df_ = DataFrame(data = {'Predicted':_res_mat_[:,0], 'Lower':_res_mat_[:,1], 'Upper':_res_mat_[:,2]},
                             columns = ['Predicted', 'Lower', 'Upper'])
        
        return _res_df_

    def residual_stderror(self, yhat):
        _ysum_ = np.sum((self.depv - yhat) ** 2)
        _sy_ = (_ysum_ * 1.) / (len(self.depv) - 2)
        return np.sqrt(_sy_)

    def yhat_ci(self, yhat, yhati, x, alpha = .05):
        _lwr_ = yhat - t.ppf(1 - (alpha / 2), len(self.depv) - 2) * self.residual_stderror(yhati) * \
                     np.sqrt(1. / len(self.indv) + ((x - self.indv.mean()) ** 2) / \
                             (np.sum((self.indv - self.indv.mean()) ** 2) * 1.))
        _upr_ = yhat + t.ppf(1 - (alpha / 2), len(self.depv) - 2) * self.residual_stderror(yhati) * \
                     np.sqrt(1. / len(self.indv) + ((x - self.indv.mean()) ** 2) / \
                             (np.sum((self.indv - self.indv.mean()) ** 2) * 1.))
        return np.column_stack((_lwr_, _upr_))

model = linear_regression(x = 'height', y = 'weight', data = women, intercept = True)
print (model)

# Output
"""
Intercept: -87.5167, Height: 3.4500
Model:
	(weight) = -87.517 +  3.450 * (height) + error

Summary:
				Estimates
	(Intercept)	  -87.517
	height		    3.450
"""

# Preidctive Values of the data points
pred = model.predict()
print (pred)


# Similar Procedures with Statsmodels
import statsmodels.api as sm

X = sm.add_constant(height)
sm_model = sm.OLS(weight, X)
results = sm_model.fit()
print(results.summary())


"""
                           OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.991
Model:                            OLS   Adj. R-squared:                  0.990
Method:                 Least Squares   F-statistic:                     1433.
Date:                Sun, 20 Jan 2019   Prob (F-statistic):           1.09e-14
Time:                        22:35:32   Log-Likelihood:                -26.541
No. Observations:                  15   AIC:                             57.08
Df Residuals:                      13   BIC:                             58.50
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        -87.5167      5.937    -14.741      0.000    -100.343     -74.691
x1             3.4500      0.091     37.855      0.000       3.253       3.647
==============================================================================
Omnibus:                        2.396   Durbin-Watson:                   0.315
Prob(Omnibus):                  0.302   Jarque-Bera (JB):                1.660
Skew:                           0.789   Prob(JB):                        0.436
Kurtosis:                       2.596   Cond. No.                         982.
==============================================================================
"""
