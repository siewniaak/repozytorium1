def process_lists(list1: list, list2: list) -> list:
    result = list(set(list1 + list2))
    result = [x**3 for x in result]
    return result
