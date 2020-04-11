import streamlit as st
import numpy as np
import seaborn as sns
from colors import *
import matplotlib.pyplot as plt
import pandas as pd
import warnings
from scipy import stats

np.random.seed(42)

# NTS i should probably make classes when i refactor since that makes more sense

warnings.warn('ignore')


def generate_page():
    st.title('Understanding Confidence Intervals and Sample Size')


@st.cache
def _get_population():
    return np.random.randint(0, 100, 100)


@st.cache
def _generate_bootstraps(population, max_value):
    '''
    TODO: there's something about this function that keeps not cacheing when compared to the power fcn...
    '''
    means = []
    for _ in range(max_value):
        sample = np.random.choice(
            population, size=len(population), replace=True)
        means.append(np.mean(sample))
    return means


def _make_plot(population, sample, confidence):
    sns.distplot(sample, color=bar_color)
    plt.ylabel('KDE Probability Density')
    plt.ylim(0, .2)
    plt.xlim(min(population), max(population))
    # confidence = float(st.text_input('Confidence Interval: ', 0.95))
    lower_bound, upper_bound = stats.norm.interval(
        confidence, np.mean(sample['bootstrap_mean']), np.std(sample['bootstrap_mean']) / np.sqrt(len(sample)))
    lower_bound = round(lower_bound, 2)
    upper_bound = round(upper_bound, 2)
    plt.axvline(x=lower_bound)
    plt.axvline(x=upper_bound)
    st.write(
        f'The {confidence} interval for the population mean is: {lower_bound, upper_bound}')
    plt.title('Bootstrapped Sample Means')
    st.pyplot()


def confidence_interval():
    '''
    Visualize how the sample size influences the confidence interval of a test statistic

    '''
    generate_page()
    max_value = 100000
    confidence = float(st.text_input('Confidence Interval', 0.95))
    population = _get_population()
    bootstraps = _generate_bootstraps(population, max_value)
    sample_size = st.radio(
        'Select the number of bootstraps:', (10, 100, 1000, 10000, max_value))
    means = pd.DataFrame(bootstraps)
    means.rename(columns={0: 'bootstrap_mean'}, inplace=True)
    sample = means.head(sample_size)
    _make_plot(population, sample, confidence)

    st.markdown('''
    As sample size increases, the range of the confidence interval for the point estimate gets smaller.
    We are able to see this as the distance between the lower bound and upper bound get smaller.
    ''')

    if st.checkbox('Show Raw Data'):
        st.write(sample)
