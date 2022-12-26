alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
executor = input()
text_words = [executor, "запретил", "букву"]
index = 0

while len(text_words[0] + text_words[1] + text_words[2]) != 0:
    plain_text = ""
    for i in text_words:
        if i != "":
            plain_text += f"{i} "
    if alphabet[index] in plain_text:
        print(f"{plain_text}{alphabet[index]}")
        for i in range(len(text_words)):
            text_words[i] = text_words[i].replace(alphabet[index], "").strip()
        index += 1
    else:
        index += 1
