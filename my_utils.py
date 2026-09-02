def get_column(file_name, query_column, query_value, result_column):
    results = []
    with open(file_name, 'r') as file:
        for line in file:
            values=line.split(',')
            if values[query_column] == query_value:
                results.append(values[result_column])
    return results

