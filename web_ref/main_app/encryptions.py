

def encrypt(data):
    data = str(data)
    result = ''

    for i in range(0, len(data)):
        result = result + chr(ord(data[i]) - 2)

    return result


def decrypt(data):
    data = str(data)
    result = ''

    for i in range(0, len(data)):
        result = result + chr(ord(data[i]) + 2)

    return result

# if __name__ == '__main__':
#     string = 'My name is Makakole'

#     x = encrypt(string)
#     print(x)
#     print('=======================')
#     y = decrypt(x)
#     print(y)