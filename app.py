import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from power import power

# importing custom colors
from colors import *

pages = ['Home', 'Power']


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
        st.title('Mo-Better')
        st.subheader('Understanding Statistical Tests and Sampling')
        st.write('(the more data the better)')
        st.write()
        st.markdown("""
        I wanted to create a better way of visualizing and explaining different statistical concepts.
        Navigate to different pages in the sidebar to check it out! :)


        """)

    if page == 'Power':
        power()


if __name__ == '__main__':
    main()
