from operator import truediv

fileArray = []


def load_file(filename):
    file = open(filename, "r")

    for line in file:
        fileArray.append(list(line))

    file.close()

    lineNum = 0
    charNum = 0
    final = 0

    for line in fileArray:
        for char in line:
            if char == "A":
                final += mas_check(int(lineNum), int(charNum), len(fileArray), len(line))
            charNum += 1
        charNum = 0
        lineNum += 1

    print(final)


def mas_check(lineNum, charNum, lineNumlen, charNumlen):
    D1 = False
    D2 = False

    if charNumlen > charNum + 2 and charNum > 0 and lineNumlen > lineNum + 1 and lineNumlen > 0:
        if char_check(fileArray[(lineNum + 1)][charNum + 1], 'M') and char_check(fileArray[(lineNum - 1)][charNum - 1], 'S'):
            D1 = True
        if char_check(fileArray[(lineNum + 1)][charNum + 1], 'S') and char_check(fileArray[(lineNum - 1)][charNum - 1], 'M'):
            D1 = True
        if char_check(fileArray[(lineNum + 1)][charNum - 1], 'M') and char_check(fileArray[(lineNum - 1)][charNum + 1], 'S'):
            D2 = True
        if char_check(fileArray[(lineNum + 1)][charNum - 1], 'S') and char_check(fileArray[(lineNum - 1)][charNum + 1], 'M'):
            D2 = True
    if D1 and D2:
        return 1
    return 0



def char_check(char, compare):
    if char == compare:
        return True
    return False


if __name__ == '__main__':
    load_file("04Input")
