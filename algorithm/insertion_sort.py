
numbers = [11, 7, 9, 23, 100, 88, 3, 21, 99, 100, 101, 32, 1, 17]

def sort(list):
    length = len(list)

    if length < 2:
        return list

    for i in numbers:
        numbers.remove(i)
        break_out = False
        for j in range(0, length-1):
            if numbers[j] >= i:
                numbers.insert(j, i)
                break_out = True
                break

        if not break_out:
            numbers.append(i)


print numbers
sort(numbers)
print numbers