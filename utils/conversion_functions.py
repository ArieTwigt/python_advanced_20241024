from typing import List, Dict
import pandas as pd
from utils import DEFAULT_COLUMNS_LIST, DEFAULT_DATA_TYPES, DEFAULT_COLUMN_NAMES


def convert_list_to_df(input_list: List[Dict], 
                       *columns: str,
                       correct_columns: bool=False,
                       **kwargs) -> pd.DataFrame:
    """
    Converts the list to a pandas DataFrame
    """

    # convert the list to a DataFrame
    df = pd.DataFrame(input_list)

    # specify the selected columns
    columns_list = DEFAULT_COLUMNS_LIST + list(columns)

    if correct_columns:
        # check if the column exists in the df
        columns_list = [column for column in columns_list if column in df.columns]
    else:
        for column in columns_list:
            if column not in df.columns:
                raise ValueError(f"The column '{column}' does not exist")

    df = df[columns_list]

    # deal with empty values
    df.dropna(subset=['catalogusprijs', 'aantal_cilinders', 'datum_tenaamstelling'], inplace=True)
    #df['catalogusprijs'].fillna(0)
    #df['catalogusprijs'].fillna(df['catalogusprijs'].mean())

    # convert to the right data types
    for column_name, data_type in DEFAULT_DATA_TYPES.items():
        df[column_name] = df[column_name].astype(data_type)

    # update the names
    for key, value in kwargs.items():
        DEFAULT_COLUMN_NAMES[key] = value


    # rename columns 
    df.rename(columns=DEFAULT_COLUMN_NAMES, inplace=True)
    
    return df