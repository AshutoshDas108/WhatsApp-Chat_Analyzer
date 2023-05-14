import matplotlib.pyplot as plt
import streamlit
from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for m in df['message']:
        words.extend(m.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for m in df['message']:
        links.extend(extract.find_urls(m))

    return num_messages, len(words), num_media_messages, len(links)

def fetch_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'Name', 'user': 'Percentage_of_Message'})

    return x, df

def create_wordcloud(selected_user, df):

    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):

    f = open('stop_words.txt', 'r')
    stop_words = f.read()

    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(25))
    return most_common_df
















