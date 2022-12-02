from constants import DATA_DIR
import ipaddress


def log_generator():
    with open(DATA_DIR) as file:
        log_sting = file.readlines()
        for log in log_sting:
            yield log


def user_filter(value, generate):
    return filter(lambda x: value in x, generate)


def user_map(num, generate):
    return map(lambda string: string.split()[int(num)], generate)


def user_unique(value, generate):
    seen = set()
    for row in generate:
        if row in seen:
            continue
        else:
            seen.add(row)
            yield row


def user_sort(order, generate):
    # reverse = None
    #
    # if order == 'asc':
    #     reverse = False
    # elif order == 'desc':
    #     reverse = True

    reverse = order == 'desc'
    return iter(sorted(generate, reverse=reverse))


def user_limit(num, generate):
    counter = 1
    for string in generate:
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
