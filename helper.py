def fetch_stats(selected_user, df):

    if selected_user != 'OverAll':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for m in df['message']:
        words.extend(m.split())
    return num_messages, len(words)








