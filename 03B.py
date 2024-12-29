import re


def load_file(filename):
    file = open(filename, "r")

    result = []
    skip_mul = False  # Flag to track DONT
    tokens = re.split(r'(don\'t\(\)|do\(\)|mul\d+)', str(file.read().replace('\n', '')))  # Split by significant tokens
    # input_string = "MUL1YDOMUL2YDODODODODODODOMUL3YDODODODODODONTDOMUL4YDONTDODONTMUL5Y"
    # tokens = re.split(r'(DONT|DO|MUL\d+)', input_string)  # Split by significant tokens
    #
    # for token in tokens:
    #     if token == "DONT":
    #         skip_mul = True  # Enable skipping MUL
    #     elif token == "DO":
    #         skip_mul = False  # Reset skip_mul
    #     elif token.startswith("MUL"):
    #         if not skip_mul:  # Append MUL only if skip_mul is False
    #             result.append(token)
    #     else:
    #         result.append(token)  # Append other non-MUL tokens

    dont = 0
    do = 0
    for token in tokens:
        if token == "don't()":
            dont += 1
            skip_mul = True  # Enable skipping MUL
        elif token == "do()":
            do += 1
            skip_mul = False  # Reset skip_mul
        elif token.startswith("mul"):
            if not skip_mul:  # Append MUL only if skip_mul is False
                result.append(token)
        else:
            result.append(token)  # Append other non-MUL tokens

    result = ''.join(result)
    print(result)

    file.close()


    findAll = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", result)
    print(findAll)

    findAll = re.findall("[0-9]{1,3}", str(findAll))
    print(findAll)

    i = 0
    final = 0
    while i < len(findAll):
        final += int(findAll[i]) * int(findAll[i + 1])

        i += 2

    file.close()

    print(final)



if __name__ == '__main__':
    load_file("03Input")




"MUL1MUL2DOMUL3MUL4DONTMUL5MUL6DOMUL7DOMUL8DONTDONTMUL9MUL10"