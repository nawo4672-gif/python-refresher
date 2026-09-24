import my_utils
import argparse
parser = argparse.ArgumentParser(description='Print the number'
                                 'of fires for a given country.')
parser.add_argument('-c', '--country', type=str, required=True,
                    help='The country to query')
parser.add_argument('-f', '--file', type=str, required=True,
                    help='The CSV file to read from')
parser.add_argument('-cc', '--country_column', type=int, default=0,
                    help='The column index for the country')
parser.add_argument('-fc', '--fires_column', type=int, default=3,
                    help='The column index for the number of fires,'
                    'default is forest fires')
parser.add_argument('-o', '--operation',
                    choices=['mean', 'median', 'standard_deviation'],
                    help='The operation to perform on the returned values')
args = parser.parse_args()


fires = my_utils.get_column(args.file, args.country_column, args.country,
                            result_column=args.fires_column)
if args.operation is None:
    print(fires)
else:
    operation = getattr(my_utils, args.operation)
    print(operation(fires))
