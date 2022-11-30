from constants import DATA_DIR


def log_generator():
    with open(DATA_DIR) as file:
        log_sting = file.readlines()
        for log in log_sting:
            yield log


def user_filter(value, generator):
    return filter(lambda x: value in x, generator)


def user_map(num, generator):
    return map(lambda string: string.split()[int(num)], generator)


def user_unique(value, generator):
    listt = []
    for string in generator:
        if string not in listt:
            listt.append(string)
            yield string


def user_sort(order, generator):
    reverse = None

    if order == 'asc':
        reverse = False
    elif order == 'desc':
        reverse = True

    return iter(sorted(generator, reverse=reverse))


def user_limit(num, generator):
    counter = 1
    for string in generator:
        if counter > num:
            break

        counter += 1

        yield string


dict_of_utils = {
    'filter': user_filter,
    'map': user_map,
    'unique': user_unique,
    'sort': user_sort,
    'limit': user_limit
}
