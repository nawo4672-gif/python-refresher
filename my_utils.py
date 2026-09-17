def get_column(file_name, query_column, query_value, result_column=1):
    results = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                values = line.split(',')
                if values[query_column] == query_value:
                    try:
                        results.append(int(values[result_column]))
                    except ValueError:
                        print(f"Could not convert '{values[result_column]}' to an integer.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return results
