import pandas as pd
import numpy as np
from datetime import datetime


# TODO 1: Clean the data - replace any NaN values
# for column in df.columns:
#     print(f"{column} nan count: {df[column].isna().sum()}")

# Only column with nan values is the postal code column - lets replace it with 'not specified'


def make_lowercase(df):
    cols_to_lower = ['Address', 'Description of Property', 'Postal Code', 'County']
    for col in cols_to_lower:
        df[col] = df[col].str.lower()
    return df


def fill_na_values(df):
    df['Postal Code'] = df['Postal Code'].fillna('not specified')
    return df

# TODO 1A: Clean the data - change the date format of our sale date column


def convert_dates_to_correct_formats(df):
    df['Date_of_Sale'] = pd.to_datetime(df['Date of Sale (dd/mm/yyyy)'], format='%d/%m/%Y')
    return df

# TODO 1B: Clean the data - convert our price column to a float


def convert_price_to_int(df):
    df['Price ()'] = df['Price ()'].str.replace('', '')
    df['Price ()'] = df['Price ()'].str.replace(',', '')
    df['Price ()'] = df['Price ()'].astype(float)
    df['Price ()'] = df['Price ()'].astype(int)
    df['Address'] = df['Address'].str.replace("'", "`")
    # df['Address'] = df['Address'].str.replace(',', '_')
    return df


# TODO 1C: Clean the data - simplofy the property description field to just second-hand or new
def group_property_type(df):
    df['Property Type'] = np.where(df['Description of Property'].str.contains('new'), 'new', 'second hand')
    return df


def fully_transform_df(df):
    make_lowercase(df)
    fill_na_values(df)
    convert_price_to_int(df)
    group_property_type(df)
    convert_dates_to_correct_formats(df)
    return df
