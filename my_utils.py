from statistics import mean as calculate_mean
from statistics import median as calculate_median
from statistics import pstdev


def mean(numbers: list[int]) -> float:
    return calculate_mean(numbers)


def median(numbers: list[int]) -> float:
    return calculate_median(numbers)


def standard_deviation(numbers: list[int]) -> float:
    return pstdev(numbers)


def get_column(file_name, query_column, query_value, result_column=1):
    results = []
    conversion_error_occurred = False
    try:
        with open(file_name, 'r') as file:
            for line in file:
                values = line.split(',')
                try:
                    if values[query_column] == query_value:
                        results.append(int(float(values[result_column])))
                except ValueError:
                    conversion_error_occurred = True
        if conversion_error_occurred:
            print("Could not convert values to an integer.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return results
