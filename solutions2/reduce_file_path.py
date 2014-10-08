def reduce_file_path(path):
    path = path.split('/')
    reduced_path = []

    for item in path:
        if item == '..':
            del reduced_path[-1]
        if item != '.' and item != '' and item != '..':
            reduced_path.append(item)
    reduced_path = '/' + '/'.join(reduced_path)

    return reduced_path
