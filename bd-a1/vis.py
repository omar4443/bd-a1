import pandas as pd
import matplotlib.pyplot as plt

def vis(input_file):
    df = pd.read_csv(input_file)

    plt.hist(df['meta_score'], bins=20, color='skyblue')
    plt.title('Meta Score Distribution')
    plt.xlabel('Meta Score')
    plt.ylabel('Frequency')
    plt.savefig('vis.png')
    plt.show()



