
numbers = [11, 7, 9, 23, 100, 88, 3, 21, 99, 100, 101, 32, 1, 17]

def sort(list):
    length = len(list)

    if length < 2:
        return list

    bucket = {}
    min_value = min(list)
    max_value = max(list)

    for i in numbers:
        if bucket.has_key(i):
            bucket[i] += 1
        else:
            bucket[i] = 1

    sorted_list = []

    for i in range(min_value, max_value+1):
        if bucket.has_key(i):
            for j in range(0, bucket[i]):
                sorted_list.append(i)

    return sorted_list

print numbers
print sort(numbers)

