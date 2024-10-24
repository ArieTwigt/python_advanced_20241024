from utils.car_import import CarImportCollection

import_collection = CarImportCollection("My Import")
import_collection.init_car_imports("audi", "bmw", "fiat", "volvo", "polestar")
import_collection.import_clean_cars()
import_collection.export_cars(combined=False)

pass
