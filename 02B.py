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
        oldTokenized = []
        oldoldTokenized = []

        for token in line.split():
            tokenized.append(int(token))
            oldTokenized.append(int(token))
            oldoldTokenized.append(int(token))

        is_desc_line = is_desc(tokenized)

        i = 1
        valid = 1

        while i < len(tokenized):
            num = tokenized[i - 1] - tokenized[i]

            if num == 0:
                tokenized.pop(i)
                valid = token_pop(tokenized)
                if not valid:
                    oldTokenized.pop(i - 1)
                    valid = token_pop(oldTokenized)
                    if not valid and i > 1:
                        oldoldTokenized.pop(i - 2)
                        valid = token_pop(oldoldTokenized)
                break

            elif is_desc_line > 0:
                if not num < 4 or not num > 0:
                    tokenized.pop(i)
                    valid = token_pop(tokenized)
                    if not valid:
                        oldTokenized.pop(i - 1)
                        valid = token_pop(oldTokenized)
                        if not valid and i > 1:
                            oldoldTokenized.pop(i - 2)
                            valid = token_pop(oldoldTokenized)
                    break

            else:
                if not num > -4 or not num < 0:
                    tokenized.pop(i)
                    valid = token_pop(tokenized)
                    if not valid:
                        oldTokenized.pop(i - 1)
                        valid = token_pop(oldTokenized)
                        if not valid and i > 1:
                            oldoldTokenized.pop(i - 2)
                            valid = token_pop(oldoldTokenized)
                    break

            i += 1

        if valid:
            validLines += 1

    return validLines


def token_pop(tokenized):
    is_desc_line = is_desc(tokenized)

    i = 1
    valid = 1
    while i < len(tokenized):
        num = tokenized[i - 1] - tokenized[i]

        if num == 0:
            return 0
        elif is_desc_line > 0:
            if not num < 4 or not num > 0:
                return 0
        else:
            if not num > -4 or not num < 0:
                return 0

        i += 1

    if valid:
        return 1



if __name__ == '__main__':
    load_file("02Input")
