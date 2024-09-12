txt_physics = ''
txt_chemistry = ''
txt_biology = ''
for i in range(len(treino.Comment)):
    if treino.Topic[i] =='Physics':
        txt_physics += treino.Comment[i]
        txt_physics += ' '
    elif treino.Topic[i] =='Chemistry':
        txt_chemistry += treino.Comment[i]
        txt_chemistry += ' '
    else:
        txt_biology += treino.Comment[i]
        txt_biology += ' '

def cleanup(txt):
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
