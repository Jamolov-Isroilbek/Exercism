plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'
plain_cipher = dict(zip(plain, cipher))

def encode(plain_text):
    plain_text = plain_text.casefold()
    cipher_text = []
    
    for ch in plain_text:
        if cipher_text and len(cipher_text) % 6 == 0:
            cipher_text.insert(-1, ' ')
        if ch.isalpha():
            cipher_text.append(plain_cipher[ch])
        elif ch.isdigit():
            cipher_text.append(ch)
        
    return ''.join(cipher_text)
    

def decode(ciphered_text):
    plain_text = []
    
    for ch in ciphered_text:
        if ch.isalpha():
            plain_text.append(plain_cipher[ch])
        elif ch.isdigit():
            plain_text.append(ch)

    return ''.join(plain_text)
