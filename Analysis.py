import pandas as pd

df = pd.read_csv("tpp_posts.csv")  
df_keyword = df[df['text'].str.contains("罷免")]
df_keyword.to_csv("tpp_dabaimian.csv", index=False)

from snownlp import SnowNLP
import pandas as pd

df = pd.read_csv("tpp_dabaimian.csv")
df['sentiment'] = df['text'].apply(lambda text: SnowNLP(text).sentiments)
def label(s): return "Positive" if s>0.6 else "Negative" if s<0.4 else "Neutral"
df['sentiment_label'] = df['sentiment'].apply(label)
df.to_csv("tpp_dabaimian_sentiment.csv", index=False)

import pandas as pd

df = pd.read_csv("tpp_dabaimian_sentiment.csv")
df['likes_count'] = df['likes']
df['comments_count'] = df['comments']
df['shares_count'] = df['shares'].fillna(0)

df['total_engagement'] = df[['likes_count','comments_count','shares_count']].sum(axis=1)

report = df.groupby('sentiment_label')[['total_engagement']].mean().reset_index()
report.to_csv("sentiment_engagement_summary.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sentiment_engagement_summary.csv")

sns.set(style="whitegrid", font_scale=1.1)

raw = pd.read_csv("tpp_dabaimian_sentiment.csv")
count_df = raw['sentiment_label'].value_counts().reset_index()
count_df.columns = ['sentiment_label', 'count']
 
plt.figure(figsize=(8,5))
sns.barplot(x='sentiment_label', y='count', data=count_df, palette='pastel')
plt.title("情感分佈")
plt.xlabel("情感类别")
plt.ylabel("贴文数量")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x='sentiment_label', y='total_engagement', data=df, palette='muted')
plt.title("按情感类别的平均互动数分佈")
plt.xlabel("情感类别")
plt.ylabel("平均互动数")
for index, row in df.iterrows():
    plt.text(index, row.total_engagement + 5, f"{row.total_engagement:.1f}", 
             ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()

