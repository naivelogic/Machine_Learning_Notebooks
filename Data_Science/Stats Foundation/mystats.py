import numpy as np
# Data Visualization
import seaborn as sns
sns.set(style="darkgrid")
import matplotlib.pyplot as plt 
from matplotlib import style

def plot_hist(data, mean=0, std=1, num_bins = 50):

    fig, ax = plt.subplots(figsize=(15,8))

    # the histogram of the data
    n, bins, patches = ax.hist(data, num_bins, density=1)

    # add a 'best fit' line
    y = ((1 / (np.sqrt(2 * np.pi) * std)) *
         np.exp(-0.5 * (1 / std * (bins - mean))**2))
    ax.plot(bins, y, '--')
    #ax.set_xlabel('Smarts')
    #ax.set_ylabel('Probability density')
    #ax.set_title(r'Histogram of pig Weights: $\mu={}$, $\sigma={}$'.format(mu, sigma))

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()
    
def descriptive_statistics_plots(data):    
    plot_hist(data, mean = np.mean(data), std = np.std(data), num_bins= 10)
    #import scipy.stats as stats
    #sns.distplot(data, kde=False, fit=stats.norm)
    #plt.show()

    fig = plt.figure(figsize=(15,8))
    plt.subplot(2, 2, 1)
    plt.title('Boxplot of Weight Dist')
    plt.boxplot(data)

    plt.subplot(2, 2, 2)
    plt.title('QQ plot')
    import scipy.stats as stats
    stats.probplot(data, plot=plt)
    plt.show()
    

def interpret(p_value, alpha_level=0.05):
    if p_value > alpha_level:
        print('Same distribution (fail to reject H0)')
    else:
        print('Different distribution (reject H0)')

def interpret_ci(ci_low, ci_high):
    if (ci_low >= 0) & (ci_high >= 0):
        print('Confidence Interval contains 0. (fail to reject H0)')
    else:
        print('Confidence Interval does not contain 0. (reject H0)')
