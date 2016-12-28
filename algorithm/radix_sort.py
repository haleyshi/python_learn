
numbers = [11, 7, 9, 23, 100, 88, 3, 21, 99, 100, 101, 32, 1, 17]

def sort(list):
    length = len(list)

    if length < 2:
        return list

    max_value = max(list)

    radix = 1
    number = max_value

    while number/10 > 0:
        number /= 10
        radix *= 10

    n = 1
    while n <= radix:
        bucket = {}
        for number in list:
            digit = number % (n*10) / n

            if bucket.has_key(digit):
                bucket[digit].append(number)
            else:
                bucket[digit] = [number]

        list = []  #shadow, not the pass-in one, so must return
        for digit in range(0, 10):
            if bucket.has_key(digit):
                for number in bucket[digit]:
                    list.append(number)

        n *= 10

    return list


print numbers
print sort(numbers)
print numbers

