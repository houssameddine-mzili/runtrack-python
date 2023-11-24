def my_long_word(length, sentence):
    
    words = []
    word = ''
    for char in sentence:
        if char == ' ' or char == ',' or char == '.':
            if word != '':
                words.append(word)
                word = ''
        else:
            word += char
    if word != '':  
        words.append(word)

    
    def word_length(word):
        count = 0
        for _ in word:
            count += 1
        return count

    
    long_words = []
    for word in words:
        if word_length(word) > length:
            long_words.append(word)


    result = ''
    first_word = True
    for word in long_words:
        if first_word:
            result += word
            first_word = False
        else:
            result += ' ' + word

    return result

output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(output)

