def calculate_mean(num_list):
    total=0
    for num in num_list:
        total=total+num
    return total/len(num_list)

if __name__ == '__main__':
    print(calculate_mean([11,45,77,88]))
