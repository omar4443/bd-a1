import pandas as pd
import numpy as np
import string
from sklearn.decomposition import PCA
from sklearn.preprocessing import KBinsDiscretizer

def dpre(input_file):
    df = pd.read_csv(input_file)
    df = df.drop_duplicates()

    df['user_review'].fillna(df['user_review'].mode().iloc[0], inplace=True)
    df['meta_score'].fillna(df['meta_score'].median(), inplace=True)

    df['release_date'] = pd.to_datetime(df['release_date'])
    df['summary'] = df['summary'].str.lower()  # Task 1: Convert to lowercase
    df['summary'] = df['summary'].str.replace(f"[{string.punctuation}]", "", regex=True)  # Task 2: Remove punctuation

    selected_features = ['name', 'platform', 'release_date', 'summary', 'meta_score', 'user_review']  # Include summary
    df = df[selected_features]

    numerical_features = ['meta_score', 'user_review']

    df = df[pd.to_numeric(df['meta_score'], errors='coerce').notna()]
    df = df[pd.to_numeric(df['user_review'], errors='coerce').notna()]

    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(df[numerical_features])
    df['pca_1'] = reduced_data[:, 0]
    df['pca_2'] = reduced_data[:, 1]

    est = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    df['meta_score_binned'] = est.fit_transform(df[['meta_score']])
    df['user_review'] = df['user_review'].astype(float)

    df['user_review_category'] = pd.cut(df['user_review'], bins=[0, 50, 75, 100], labels=['Low', 'Medium', 'High'])

    df.to_csv("res_dpre.csv", index=False)

    return "res_dpre.csv"


