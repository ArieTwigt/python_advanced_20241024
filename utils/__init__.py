import os

ENDPOINT = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
DATA_FOLDER = "data"

DEFAULT_COLUMNS_LIST = ['merk', 'handelsbenaming', 'catalogusprijs', 
                        'datum_tenaamstelling', 'aantal_cilinders', 'eerste_kleur']

# change the data types
DEFAULT_DATA_TYPES = {"catalogusprijs": float,
                     "aantal_cilinders": int}

# default column names
DEFAULT_COLUMN_NAMES = {"catalogusprijs": "prijs",
                        "handelsbenaming": "model"}

if not os.path.exists(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)
    print(f"Created: {DATA_FOLDER}")