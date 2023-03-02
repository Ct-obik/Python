# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# INPUT: She sells sea shells on the sea shore The shells
# that she sells are sea. Sells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
# from string import punctuation

d = set("""She sells sea shells on the sea shore The shells
that she sells are sea. Sells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea shore shells""".replace("."," ").lower().split())
print(len(d))