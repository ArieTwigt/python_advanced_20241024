import pandas as pd
import os
from utils import DATA_FOLDER
from datetime import datetime


def export_df_to_csv(df: pd.DataFrame, 
                     brand_name: str) -> None:
    '''
    Exports the pandas DataFrame to csv
    '''

    # create the folder name
    folder_path = f"{DATA_FOLDER}/{brand_name}"
    os.makedirs(folder_path, exist_ok=True)

    # create a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # define the file path
    file_path = f"{folder_path}/export_{timestamp}_{brand_name}.csv"

    # expor the csv
    df.to_csv(file_path, index=False)
    print(f"✅ Exported {file_path}")