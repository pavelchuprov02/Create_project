def str_func(word):
    """Пропись строчных букв"""
    return word.upper()

def new_func(word_tittle):
    """Слово с заглавной буквы"""
    return word.title()

word = str_func("high_str")
word_title = new_func("high_str")

print(word)
print(word_title)
