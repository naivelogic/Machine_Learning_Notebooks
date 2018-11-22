# Basic Example for performing a T Test
## .. source: Statistisc and Machine Learning in Python
## Scenario: Given the following samples, test whether the true mean is 1.75

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1.83, 1.83, 1.73, 1.82, 1.83, 1.73, 1.99, 1.85, 1.68, 1.87] # sample population

xbar = np.mean(x)       # sample mean
mu0 = 1.75              # hypothesized value
s = np.std(x, ddof=1)   # sample standard deviation
n = len(x)              # sample size

tobs = (xbar - mu0) / (s / np.sqrt(n))      # t-statistic
print(tobs)

# calculate the t-value
tvalues = np.linspace(-10, 10, 100)
plt.plot(tvalues, stats.t.pdf(tvalues, n-1), 'b-', label="T(n-1)")
upper_tval_tvalues = tvalues[tvalues > tobs]
plt.fill_between(upper_tval_tvalues, 0, stats.t.pdf(upper_tval_tvalues, n-1), alpha = .9, label="p-value")
_ = plt.legend()
