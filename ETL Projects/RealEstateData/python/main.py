from extract import extract_data
from transform import fully_transform_df


if __name__ == '__main__':
    # EXTRACT
    trial = extract_data()
    # TRANSFORM
    clean = fully_transform_df(trial)
    # LOAD
