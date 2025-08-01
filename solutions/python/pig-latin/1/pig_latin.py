def translate(text):
    vowels = 'aeiou'
    suffix = 'ay'
    result = ''
    
    for word in text.split(' '):
        prefix = ''

        for i in range(len(word)):
            ch = word[i]        
        
            if ch not in vowels: 
                if ch == 'y' and prefix:
                    result += word[i:] + prefix + suffix
                    break
            
                prefix += ch
            
                if prefix == 'xr' or prefix == 'yt':
                    result += word + suffix 
                    break
            
            elif ch == 'u' and prefix and prefix[-1] == 'q':
                prefix += ch
            else:
                result += word[i:] + prefix + suffix
                break

        result += ' '

    return result.strip()