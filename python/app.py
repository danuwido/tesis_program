import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk


df = pd.read_csv('phyton/data_billing-acc-telemarketing2.csv')
df.shape

df_feature = df.drop('Outcome',1)
sr_outcome = df['Outcome']
pd.set_option('display.max_columns',None)

from  sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

chi2_selector = SelectKBest(chi2, k=6) 
chi2_selector.fit(df_feature, sr_outcome)



cols = chi2_selector.get_support(indices=True)
df_selected_features = df_feature.iloc[:,cols]

df_selected_features.head()

#print(df_selected_features.head())