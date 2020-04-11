import streamlit as st
from power import power
from confidence_interval import confidence_interval

pages = ['Home', 'Confidence Intervals']


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

    if page == 'Confidence Intervals':
        print('data again')
        confidence_interval()

    if page == 'Power':
        print('entered power')
        power()


if __name__ == '__main__':
    main()
