import pandas
df = pandas.read_csv('/Users/19luc/OneDrive/Desktop/Test_01/Book2.csv')
df = df.drop([3], axis=0)
df['source'] = ['excel', 'class', 'verzeo', 'training']

print(df)
# df.to_csv('/Users/19luc/OneDrive/Desktop/Book2.csv')
