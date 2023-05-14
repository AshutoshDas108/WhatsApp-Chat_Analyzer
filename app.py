import streamlit as st
import preprocessor
import helper
import pandas as pd

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    #st.text(data)
    df = preprocessor.preprocess(data)
    st.dataframe(df)

    # fetch unique users

    user_List = df['user'].unique().tolist()
    user_List.remove('group_notification')
    user_List.sort()
    user_List.insert(0,'OverAll')

    selected_user = st.sidebar.selectbox("show analysis wrt", user_List)

    if st.sidebar.button("Show Analysis"):

        num_messages, words = helper.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.beta_columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)



