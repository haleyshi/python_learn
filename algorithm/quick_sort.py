

numbers = [11, 7, 9, 23, 100, 88, 3, 21, 99, 100, 101, 32, 1, 17]

def sort(list):
    length = len(list)

    if length < 2:
        return list

    seed = list[0]

    left_list = []
    right_list = []
    sorted_list = []

    for i in range(1, length, 1):
        if list[i] > seed:
            right_list.append(list[i])
        else:
            left_list.append(list[i])

    for x in sort(left_list):
        sorted_list.append(x)
    sorted_list.append(seed)
    for x in sort(right_list):
        sorted_list.append(x)

    return sorted_list


print numbers
print sort(numbers)



