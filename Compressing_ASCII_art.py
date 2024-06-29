import json 

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

'''
# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

    data = [f'{char}|{count}' for char, count in data]

    with open(newFilename, 'w') as f:
        f.write('~'.join(data))
    pass

def decodeFile(filename):
    with open(filename) as f:
        data = f.read()

    pairs = data.split('~')
    pairs = [p.split('|') for p in pairs]
    pairs = [(p[0], int(p[1])) for p in pairs]
    return decodeString(pairs)
    pass
    '''
    
# Byte solution
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())
    output = bytearray()
    for item in data:
        # Character byte
        output.extend(bytes(item[0], 'utf-8'))
        #Integer count byte
        output.extend(item[1].to_bytes(1, 'big'))
    with open(newFilename, 'wb') as binary_file:
        # Write bytes to file
        binary_file.write(output)
    
def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        # Split data into pairs
        bytePairs = [data[i:i+2] for i in range(0, len(data), 2)]
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[:1].decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
        return decodeString(encodedList)
