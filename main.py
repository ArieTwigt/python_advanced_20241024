from utils.import_functions import import_car_by_brand
from utils.conversion_functions import convert_list_to_df
from utils.export_functions import export_df_to_csv
from argparse import ArgumentParser

# initiate an argument parsers
parser = ArgumentParser()

# add arguments to the parser
parser.add_argument("--brand", "-b",
                  required=True,
                  help="Name of the brand to import")

parser.add_argument("--rows", "-r",
                    required=False,
                    default=3,
                    type=int,
                    help="How many rows to display")

parser.add_argument("--export", "-e",
                    required=False,
                    default="print",
                    type=str,
                    choices=("print", "csv", "database"),
                    help="How to export the results")


# parse the arguments
args = parser.parse_args()


# import cars
cars_list =  import_car_by_brand(args.brand)

# convert the list to a DataFrame
cars_df = convert_list_to_df(cars_list, "inrichting", "voertuigsort", correct_columns=True,
                   catalogusprijs="betaling",
                   aantal_cilinders="cilinders")

# export
if args.export == "print":
    print(cars_df.head(args.rows))
elif args.export == "csv":
    export_df_to_csv(cars_df, args.brand)
else:
    print("Written do database")