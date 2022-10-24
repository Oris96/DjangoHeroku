alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = input()
phrase = f'запретил букву'

for i in range(len(alphabet)):
    if alphabet[i] in list(word + phrase):
        if phrase:
            print(f'{word} {phrase} {alphabet[i]}'.strip())
        else:
            print(f'{word} {alphabet[i]}'.strip())
        word = word.replace(alphabet[i], '')
        phrase = phrase.replace(alphabet[i], '').strip()
        