def load_file(filename):
    file = open(filename, "r")
    validLines = read_by_tokens(file)
    file.close()
    print(validLines)


def is_desc(array):
    num = array[0] - array[1]
    return num


def read_by_tokens(fileobj):
    validLines = 0
    for line in fileobj:
        tokenized = []
        for token in line.split():
            tokenized.append(int(token))

        is_desc_line = is_desc(tokenized)

        if is_desc_line == 0:
            continue

        i = 1
        valid = 1
        while i < len(tokenized):
            num = tokenized[i - 1] - tokenized[i]

            if num == 0:
                valid = 0
            elif is_desc_line > 0:
                if not num < 4 or not num > 0:
                    valid = 0
            else:
                if not num > -4 or not num < 0:
                    valid = 0

            i += 1

        if valid:
            validLines += 1

    return validLines



if __name__ == '__main__':
    load_file("02Input")
