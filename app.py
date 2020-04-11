import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
from power import power
#
# # importing custom colors
# from colors import *

pages = ['Home', 'Power']


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
