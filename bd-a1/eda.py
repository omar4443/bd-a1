import pandas as pd

def eda(input_file):
    df = pd.read_csv(input_file)

    insight_1 = "Correlation\n"
    numeric_columns = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_columns.corr()
    insight_1 += str(correlation_matrix)

    insight_2 = "Summary Statistics\n"
    summary_stats = df.describe()
    insight_2 += str(summary_stats)

    insight_3 = "Value Counts\n"
    value_counts = df['platform'].value_counts()
    insight_3 += str(value_counts)

    with open('eda-in-3.txt', 'w') as file1:
        file1.write(insight_1)

    with open('eda-in-1.txt', 'w') as file2:
        file2.write(insight_2)

    with open('eda-in-2.txt', 'w') as file3:
        file3.write(insight_3)



