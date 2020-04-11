import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from power import power

# importing custom colors
from colors import *

pages = ['Home', 'Power', 'Stats Analysis', 'Sampling']


@st.cache
def generate_data(n_columns=10, n_rows=10000):
    data = []
    letter_list = ['a', 'b', 'c', 'd', 'e']
    options = ['letters', 'numbers']
    for _ in range(n_columns):
        type = np.random.choice(options)
        if type == 'letters':
            data.append(np.random.randint(0, 100, n_rows))
        else:
            data.append(np.random.choice(letter_list, n_rows))
    df = pd.DataFrame(data).T  # this seems to be faster than vstack
    df.columns = [f'column_{num}' for num in range(len(df.columns))]
    print('generating data again')
    return df


def main():
    page = st.sidebar.selectbox('Pages', pages)
    if page == 'Home':
        st.title('Welcome to Understanding Uncertainty & Sampling')

    if page == 'Power':
        power()


if __name__ == '__main__':
    main()
