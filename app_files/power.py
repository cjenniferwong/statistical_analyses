import streamlit as st
import numpy as np
import seaborn as sns
from colors import *
import matplotlib.pyplot as plt
import pandas as pd
import warnings

warnings.warn('ignore')


def generate_page():
    st.title('Understanding how sample size affects power of experiements')
    st.subheader(
        'Recall that power denotes the ability to reject the null hypothesis when the null hypothesis is not true')
    st.write('''You can think of it as the ability to not make false negatives.
    ''')


@st.cache
def generate_data(mean, sample_size):
    data = np.random.normal(mean, size=sample_size)
    return data


def power():
    generate_page()
    st.markdown('''There are 4 parts to Power Analysis:''')
    st.write('- significance (tolerance for false positives)')
    st.write('- sample sizes')
    st.write('- effect size')
    st.write('- statisical power (tolerance for false negatives)')
    st.write()
    st.write('Below, we will visualize how sample sizes affect statisical power')
    mean_a = int(st.text_input('Enter mean for A:', 0))
    # std_a = int(st.text_input('Enter std for A:', 1))
    mean_b = int(st.text_input('Enter mean for B:', 0))
    # std_b = int(st.text_input('Enter std for B:', 1))
    # sig = float(st.text_input('Enter the significance: ', 0.05))

    max_value = 10000
    data_a = generate_data(mean_a, max_value)
    data_b = generate_data(mean_b, max_value)
    choice = st.slider('Select the sample size for a and b',
                       min_value=1, max_value=max_value)
    data = pd.DataFrame([data_a, data_b]).T
    data.rename(columns={
        0: 'sample_a', 1: 'sample_b'
    }, inplace=True)

    sample = data.head(choice)

    sns.distplot(sample['sample_a'], norm_hist=True)
    sns.distplot(sample['sample_b'], color=bar_color, norm_hist=True)
    plt.ylim(0, 1)
    plt.title('Sample Distribution')
    plt.xlabel('')

    st.pyplot()

    if st.checkbox('Show raw data:'):
        st.dataframe(sample)

    st.markdown("""As we increase the sample size, the more representative our sample will be of the population.
    This enhances our ability to detect an effect if indeed the effect is present.
    This is the definition of power! Therefore as our sample size increases, our power increases.
    """)
    st.markdown('''
    ## Great! So we should always just gather as much data as we can to maximize the power of our test!
    That would be true, but there are trade-offs to consider. Note that the longer the experiment,
    the more time and money is needed gather the data. This is why power analyses are useful!
    We can identify the minimum sample size needed to conduct out experiement given these a set of constraints.

    ''')
