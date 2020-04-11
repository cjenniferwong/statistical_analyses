import streamlit as st
import numpy as np
import seaborn as sns
from colors import *
import matplotlib.pyplot as plt
import pandas as pd


def generate_page():
    st.title('Understanding how sample size affects power of experiements')
    st.subheader(
        'Recall that power denotes the ability to reject the null hypothesis when the null hypothesis is not true')
    st.write('''You can think of it as the ability to not make false negatives.
    ''')


@st.cache
def generate_data(mean, std, sample_size):
    data = np.random.normal(mean, std, sample_size)
    return data


def power():
    generate_page()
    mean_a = int(st.text_input('Enter mean for A:'))
    std_a = int(st.text_input('Enter std for A:'))
    mean_b = int(st.text_input('Enter mean for B:'))
    std_b = int(st.text_input('Enter std for B:'))

    max_value = 100
    data_a = generate_data(mean_a, std_a, max_value)
    data_b = generate_data(mean_b, std_b, max_value)
    choice = st.slider('Select the sample size', min_value=1, max_value=max_value)
    data = pd.DataFrame([data_a, data_b]).T
    data.rename(columns={
        0: 'sample_a', 1: 'sample_b'
    }, inplace=True)

    sample = data.head(choice)

    sns.distplot(sample['sample_a'], norm_hist=True)
    sns.distplot(sample['sample_b'], color=bar_color, norm_hist=True)
    plt.ylim(0, 1)
    plt.title('Sample Distribution')

    st.pyplot()

    if st.checkbox('Show raw data:'):

        st.dataframe(sample)
