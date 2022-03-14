import sqlite3
import pandas as pd


# # TODO 1: Connect / Create Real Estate Purchases DB
# con = sqlite3.connect('real_estate_purchase_data.db')
# cur = con.cursor()
#
#
#
# # TODO 1A: Create a county table (we can enrich this data in the future with county demographic data)
# cur.execute('''CREATE TABLE counties
#             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             county_name text)''')
#
# con.commit()
#
#
# # TODO 1B: Create a purchases table
#
# cur.execute('''CREATE TABLE purchases
#                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                date_of_sale_yyyy_mm_dd text not null,
#                address text not null,
#                postal_code text not null,
#                county text not null,
#                price_euros integer not null,
#                property_description text not null,
#                property_type text not null,
#                county_id integer not null,
#                FOREIGN KEY(county_id) REFERENCES counties(id))''')
#
# # Create the Table
# con.commit()
# con.close()

con = sqlite3.connect('real_estate_purchase_data.db')
cur = con.cursor()

# TODO 2: Load county data


def load_county_data(df):
    county_data = df['County'].unique()
    for county_name in county_data:
        cur.execute("INSERT INTO counties (county_name)"
                    f"VALUES ('{county_name}')")
    con.commit()

# #TODO 3: Load DF data


def load_purchase_data(df):
    for index, row in df.iterrows():
        date = row['Date_of_Sale']
        address = row['Address']
        postal = row['Postal Code']
        county = row['County']
        price = int(row['Price ()'])
        description = row['Description of Property']
        prop_type = row['Property Type']
        county_id = cur.execute(f"SELECT id FROM counties WHERE county_name = '{county}'").fetchone()[0]

        cur.execute("INSERT INTO purchases (date_of_sale_yyyy_mm_dd, address, postal_code, county, price_euros, property_description, property_type, county_id) "
                    f"VALUES ('{date}', '{address}', '{postal}', '{county}', '{price}', '{description}', '{prop_type}', '{county_id}')")

        con.commit()

    con.close()


def load_all_data(df):
    load_county_data(df)
    load_purchase_data(df)
    con.close()
