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
            if char == "X":
                final += xmas_check(int(lineNum), int(charNum), len(fileArray), len(line))
            charNum += 1
        charNum = 0
        lineNum += 1

    print(final)


def xmas_check(lineNum, charNum, lineNumlen, charNumlen):
    local = 0
    # HORIZONTAL 2
    if charNumlen > charNum + 3:
        if char_check(fileArray[lineNum][charNum + 1], 'M') and char_check(fileArray[lineNum][charNum + 2], 'A') and char_check(
                fileArray[lineNum][charNum + 3], 'S'):
            local += 1
    if charNum - 3 > - 1:
        if char_check(fileArray[lineNum][charNum - 1], 'M') and char_check(fileArray[lineNum][charNum - 2], 'A') and char_check(
                fileArray[lineNum][charNum - 3], 'S'):
            local += 1
    # VERTICAL 2
    if lineNumlen > lineNum + 3:
        if char_check(fileArray[(lineNum + 1)][charNum], 'M') and char_check(fileArray[(lineNum + 2)][charNum], 'A') and char_check(
                fileArray[(lineNum + 3)][charNum], 'S'):
            local += 1
    if lineNum - 3 > - 1:
        if char_check(fileArray[(lineNum - 1)][charNum], 'M') and char_check(fileArray[(lineNum - 2)][charNum], 'A') and char_check(
                fileArray[(lineNum - 3)][charNum], 'S'):
            local += 1
    # DIAGONAL 4
    if charNumlen > charNum + 3 and lineNumlen > lineNum + 3:
        if char_check(fileArray[(lineNum + 1)][charNum + 1], 'M') and char_check(fileArray[(lineNum + 2)][charNum + 2], 'A') and char_check(
                fileArray[(lineNum + 3)][charNum + 3], 'S'):
            local += 1
    if charNum - 3 > - 1 and lineNum - 3 > - 1:
        if char_check(fileArray[(lineNum - 1)][charNum - 1], 'M') and char_check(fileArray[(lineNum - 2)][charNum - 2], 'A') and char_check(
                fileArray[(lineNum - 3)][charNum - 3], 'S'):
            local += 1
    if charNum - 3 > - 1 and lineNumlen > lineNum + 3:
        if char_check(fileArray[(lineNum + 1)][charNum - 1], 'M') and char_check(fileArray[(lineNum + 2)][charNum - 2], 'A') and char_check(
                fileArray[(lineNum + 3)][charNum - 3], 'S'):
            local += 1
    if charNumlen > charNum + 3 and lineNum - 3 > - 1:
        if char_check(fileArray[(lineNum - 1)][charNum + 1], 'M') and char_check(fileArray[(lineNum - 2)][charNum + 2], 'A') and char_check(
                fileArray[(lineNum - 3)][charNum + 3], 'S'):
            local += 1
    return local


def char_check(char, compare):
    if char == compare:
        return True
    return False


if __name__ == '__main__':
    load_file("04Input")
