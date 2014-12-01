def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    test = len(aStr) / 2
    if (aStr == '') or (len(aStr) == 1) and (aStr != char):
        return False
    elif aStr[test] == char:
        return True
    elif aStr[test] < char:
        aStr = aStr[test:]
        return isIn(char, aStr)
    else:
        aStr = aStr[:test]
        return isIn(char, aStr)