def calculate_multiple(factor):
    multiple_list = list()

    for num in range(2, 101):
        if num % factor == 0:
            multiple_list.append(num)
    return multiple_list


if __name__ == '__main__':
    multiple_dict = dict()
    for factor in range(2, 10):
        multiple_dict[factor] = calculate_multiple(factor)
    print(multiple_dict)
