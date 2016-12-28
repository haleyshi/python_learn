

numbers = [11, 7, 9, 23, 100, 88, 3, 21, 99, 100, 101, 32, 1, 17]


def sort(list):
    length = len(list)

    print "length:", length

    if length < 2:
        return

    compare = 0
    swap = 0

    while length > 1:
        for i in range(0, length-1, 1):
            compare += 1
            if list[i] > list[i+1]:
                swap += 1
                bigger = list[i]
                list[i] = list[i+1]
                list[i+1] = bigger

        length -= 1

    print "compare:", compare
    print "swap:", swap


print numbers
sort(numbers)
print numbers