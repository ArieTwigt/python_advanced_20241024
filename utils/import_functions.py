import requests
from utils import ENDPOINT
from typing import List, Dict


def import_car_by_brand(brand: str) -> List[Dict]:
    """
    Function to import a car by brand:
    
    * brand: brand of the car to import
    """


    # check for the right type
    if type(brand) != str:
        raise TypeError(f"Wrong type, should be 'str', got {type(brand)}")
    

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = ENDPOINT + f"?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data from the response
    data = response.json()

    # check if the data is empty
    if len(data) == 0:
        raise ValueError(f"No cars found for '{brand}' ")
        
    
    return data