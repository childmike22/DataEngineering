from extract import extract_data
from transform import fully_transform_df
from load import load_all_data


if __name__ == '__main__':
    # EXTRACT
    extracted_data = extract_data()
    # TRANSFORM
    data_to_load = fully_transform_df(extracted_data)
    # LOAD
    load_all_data(data_to_load)
