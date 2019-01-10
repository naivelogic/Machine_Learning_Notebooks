#################
# This is a set of statistical functions that I used to perform statistical inference 
# including: 
# - normality testing with Hist, QQ Plots and Boxplots
# - Hypothesis testing: T-test, ANOVA and interpretation of CI and Pvalue

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

    #####  QQ / Normal Probability Plots   #######
    ## The nromal probability plot is a graphical technique to identify substantive departures from normality
    ## It is based on the comparision between the observed deistribution and the theoretical distributions
    ## .. under the normal assumption. 
    ## The null hypothesis (normal distribution) is rejected if the points are ont aligned on a stright line
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

def my_ttest(mu_1, s_1, n_1, mu_2, s_2, n_2, alpha=0.05):
    # Two Sample T Test
    from scipy import stats

    # General Stats

    ## Sample Data 1
    data1 = stats.t.rvs(loc=mu_1, scale=s_1, df=(n_1-1), size=n_1)

    ## Sample Data 2
    data2 = stats.t.rvs(loc=mu_1, scale=s_1, df=(n_1-1), size=n_1)


    df_ = n_1 + n_2 - 2
    alpha = alpha

    # plot distribution for normality
    mystats.descriptive_statistics_plots(data1)
    mystats.descriptive_statistics_plots(data2)


    # tt = (sm-m)/np.sqrt(sv/float(n))  # t-statistic for mean
    tt = (mu_1 - mu_2) / (np.sqrt(((s_1**2)/n_1) + ((s_2**2)/n_2)))
    print("T Test Score: ", tt)

    #Studnt, n=14, p<0.05, 2-tail
    t_crit = stats.t.ppf(1-alpha/2, df_)
    print("T Critical Value: ", t_crit)

    # p value two sided 
    pval = stats.t.sf(np.abs(tt), df_)*2
    print("p-value: ", pval)

    # confidence interval
        ## Pooled Standard Deviaiton
    sp = np.sqrt((((n_1-1)*(s_1**2)) + ((n_2-1)*(s_2**2)))/df_ ) # pooled variance (ratio of variances is less than 1)
    se = sp * np.sqrt((1/n_1 + 1/n_2))

    diff_ = mu_1 - mu_2

    ci_low = diff_ - (t_crit * se)
    ci_high = diff_ + (t_crit * se)
    print("Confidence Interval from: %.3f to %.3f" % (ci_low, ci_high))
