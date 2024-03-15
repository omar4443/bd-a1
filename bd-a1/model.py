import pandas as pd
from sklearn.cluster import KMeans

def model(input_file):
    df = pd.read_csv(input_file)

    selected_columns = ['meta_score', 'user_review']
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(df[selected_columns])
    cluster_counts = df['cluster'].value_counts()
    cluster_counts.to_csv("k.txt", header=['count'], index_label='cluster', sep='\t')
    print(cluster_counts)


