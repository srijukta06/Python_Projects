def encodeString(stringVal):
    encodedList = [] 
    prevChar = stringVal[0] 
    count = 0
    for char in stringVal: 
        if prevChar != char: 
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
    pass
