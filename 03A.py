import re


def load_file(filename):
    file = open(filename, "r")

    findAll = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", str(file.read().replace('\n', '')))

    findAll = re.findall("[0-9]{1,3}", str(findAll))

    i = 0
    final = 0
    while i < len(findAll):
        final += int(findAll[i]) * int(findAll[i + 1])

        i += 2

    file.close()

    print(final)



if __name__ == '__main__':
    load_file("03Input")
