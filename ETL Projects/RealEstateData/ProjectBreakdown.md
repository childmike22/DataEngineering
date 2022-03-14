## The following project is a simple ETL job on real estate data from a DataCamp course

[ETL in Python Course](https://campus.datacamp.com/courses/etl-in-python/explore-the-data-and-requirements?ex=1 "DataCamp Course")

### [1) Extract](https://github.com/childmike22/DataEngineering/blob/main/ETL%20Projects/RealEstateData/python/extract.py)
  - The extract job pulls data from a URL that automatically downloads a zipfile
  - Accessible for historical audits / and we have access to the original zip file

### [2) Transform](https://github.com/childmike22/DataEngineering/blob/main/ETL%20Projects/RealEstateData/python/transform.py)
  - Normal data cleansing (removing null or NaN values and converting data types (dates, floats, ints, etc)
  - Grouping large text data into simplified 'property types' (new or second hand)

### [3) Load](https://github.com/childmike22/DataEngineering/blob/main/ETL%20Projects/RealEstateData/python/load.py)
  - Create a 'real_estate_purchases' db
  - Create two tables (purchase and counties)
  - Counties looks at unique counties in the data set. Ideally we would use 3rd party data on demographics (age, crime rates, gender, education levels, quality of local schools, etc) to deepen our understanding of these house prices
  - Load all purchase / county data into our DB and now we have a functioning database!

### [Final Script](https://github.com/childmike22/DataEngineering/blob/main/ETL%20Projects/RealEstateData/python/main.py)
