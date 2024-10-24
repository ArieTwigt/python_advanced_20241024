from typing import List, Dict
from utils import ENDPOINT, DEFAULT_COLUMNS_LIST, DEFAULT_DATA_TYPES, \
                  DEFAULT_COLUMN_NAMES, DATA_FOLDER
import requests
import pandas as pd
import os
from datetime import datetime
from tqdm import tqdm


class CarImport:

    def __init__(self, brand: str):
        self.brand = brand
        self.data = []
        self.df = pd.DataFrame()

    
    def import_car_by_brand(self) -> List[Dict]:
        """
        Function to import a car by brand:
        
        * brand: brand of the car to import
        """


        # check for the right type
        if type(self.brand) != str:
            raise TypeError(f"Wrong type, should be 'str', got {type(self.brand)}")
        

        # uppercase the brand
        brand_upper = self.brand.upper()

        # define the endpoint
        endpoint = ENDPOINT + f"?merk={brand_upper}"

        # execute the request
        response = requests.get(endpoint)

        # get the data from the response
        data = response.json()

        # check if the data is empty
        if len(data) == 0:
            raise ValueError(f"No cars found for '{self.brand}' ")
            
        
        # add to the data list
        self.data += data



    def convert_list_to_df(self, 
                       *columns: str,
                       correct_columns: bool=False,
                       **kwargs) -> pd.DataFrame:
        """
        Converts the list to a pandas DataFrame
        """

        # convert the list to a DataFrame
        df = pd.DataFrame(self.data)

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
        
        # add to self
        self.df = df


    def export_df_to_csv(self) -> None:
        '''
        Exports the pandas DataFrame to csv
        '''

        # create the folder name
        folder_path = f"{DATA_FOLDER}/{self.brand}"
        os.makedirs(folder_path, exist_ok=True)

        # create a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # define the file path
        file_path = f"{folder_path}/export_{timestamp}_{self.brand}.csv"

        # expor the csv
        self.df.to_csv(file_path, index=False)
        print(f"✅ Exported {file_path}")

    
    def __repr__(self) -> str:
        return f"Import {self.brand} - Rows: {len(self.df)}"


class CarImportCollection:

    def __init__(self, 
                 name: str, 
                 export_type: str="csv"):
        self.name = name
        self.export_type = export_type
        self.car_import_list = []

    def init_car_imports(self, *brands):
        for brand in brands:
            car_import = CarImport(brand)
            self.car_import_list.append(car_import)

    
    def import_clean_cars(self):
        for car in tqdm(self.car_import_list):
            car.import_car_by_brand()
            car.convert_list_to_df()
            

    def export_cars(self, combined=True, file_name=""):
        if combined:
            # collect the seperate DataFrames
            df_list = [car.df for car in self.car_import_list]

            # combine the seperate DataFrames
            df_combined = pd.concat(df_list)
            
            # define the file path
            if file_name == "":
                brands_list = [car.brand for car in self.car_import_list]
                file_name = "_".join(brands_list)

            # folder path
            os.makedirs(f"{DATA_FOLDER}/combined", exist_ok=True)

            # compose the file path
            file_path = f"{DATA_FOLDER}/combined/{file_name}.csv"
            
            
            # export
            df_combined.to_csv(file_path, index=False)
            print(f"Succesfully exported {file_path}")
        else:
            for car in self.car_import_list:
                car.export_df_to_csv()
            