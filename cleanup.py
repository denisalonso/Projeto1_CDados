def cleanup2(txt):
    new_txt = ''
    clean_txt = txt.replace('\\n',' ')
    split_txt = clean_txt.split(' ')
    for word in split_txt:
        if 'https' not in word:
            new_word = ''
            for character in word:
                if character.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
                    new_word += character.lower()
            if new_word != '':
                new_txt += ' '
                new_txt += new_word
    return new_txt.strip()