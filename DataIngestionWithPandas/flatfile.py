import pandas as pd

# Specify relevant columns
col_names = ['STATEFIPS', 'STATE', 'zipcode', 'agi_stub', 'N1']


# Create dataframe (with selected columns) and specify datatypes when needed
tax_data_vermont = pd.read_csv('https://assets.datacamp.com/production/repositories/4412/datasets/61bb27bf939aac4344d4f446ce6da1d1bf534174/vt_tax_data_2016.csv',
                               usecols=col_names, dtype={'zipcode': str},
                               na_values={'zipcode': 0})

# TODO 1: idenfity core fundamentals of this dataframe
print(tax_data_vermont.columns)
print(tax_data_vermont.dtypes)
print(tax_data_vermont.head(20))
