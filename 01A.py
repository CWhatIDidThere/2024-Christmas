array1 = []
array2 = []
final = 0


def load_file_read_by_line(filename):
    file = open(filename, "r")

    for line in file:
        split = line.split()
        array1.append(int(split[0]))
        array2.append(int(split[1]))
    file.close()


if __name__ == '__main__':
    load_file_read_by_line("01Input")
    # sorted
    array1.sort()
    array2.sort()

    i = len(array1)

    while i > 0:
        final += abs(array2[i - 1] - array1[i - 1])
        i -= 1

    print(final)
