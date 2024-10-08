def replace(input_list):
    mempory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = mempory

    return input_list

print(replace([1, 2, 3, 4, 5]))