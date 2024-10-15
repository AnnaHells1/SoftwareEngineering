def tuple_sort(tpl):
    if not all(isinstance(elm, int) for elm in tpl):
        return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, "1", 9)))