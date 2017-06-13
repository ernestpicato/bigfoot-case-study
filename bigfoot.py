import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup


json_data = open('bigfoot_data.json', 'rw+')
with open('bigfoot_data.json') as f:
    data = json_data.readlines()

max_features = 0
for i in xrange(len(data)):
    soup = BeautifulSoup(data[i], 'html.parser')
    num_features = len(soup.find_all("p"))
    if num_features > max_features:
        max_features = num_features
        most_feature_index = i

soup = BeautifulSoup(data[most_feature_index],'html.parser')
p = soup.find_all("p")
num_features = len(p)
features = []
for i in xrange(num_features):
    if p[i].span != None:
        feature = p[i].span.get_text()
        features.append(feature)


df = pd.DataFrame(index=np.arange(len(data)), columns=features)

titles = []
for i in xrange(len(data)):
    soup = BeautifulSoup(data[i], 'html.parser')
    titles.append(soup.title.get_text())
    p = soup.find_all("p")
    for j in xrange(len(p)):
        if p[j].span != None:
            for feature in features:
                if p[j].span.get_text() == feature:
                    df[feature][i]= p[j].get_text().split(p[j].span.get_text())[1]

df['Title'] = pd.Series(titles)

print df.head()
