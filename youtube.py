import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('INvideos.csv' , encoding='latin1')

data=data.drop(['description','thumbnail_link','tags'],axis=1)

# Top 5 most views youtube channel
top_chann=data.groupby('channel_title').agg({'views':"sum"}).sort_values(by='views',ascending=False).head(5)
sns.barplot(data=top_chann,x='channel_title',y='views')
plt.show()

top_vid=data.groupby('title').agg({'views':"sum"}).sort_values(by='views',ascending=False).head(5)

sns.barplot(data=top_vid,x='title',y='views')
plt.xlabel()
plt.xticks(rotation=10)
plt.show()

data.to_csv("youtube.csv")

print(top_vid)