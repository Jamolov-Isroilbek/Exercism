def rotate(text, key):
    key %= 26

    ord_a, ord_z = ord('a'), ord('z')
    ord_A, ord_Z = ord('A'), ord('Z')

    result = ''
    
    for i in text:
        if i.isalpha():
            temp = ord(i) + key
            if i.islower():
                if temp > ord_z:
                    temp = ord_a + temp - ord_z - 1 
            else:
                if temp > ord_Z:
                    temp = ord_A + temp - ord_Z - 1
                             
            result += chr(temp)
        else:
            result += i

    return result 