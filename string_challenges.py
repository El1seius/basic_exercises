# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
quantity_vowels = 0
for letter in word.lower():
    if letter in vowels:
        quantity_vowels += 1
print(quantity_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(" ")))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_word = sentence.split(" ")
for element in sentence_word:
    print(element[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_word = sentence.split(" ")
general_length = 0
for element in sentence_word:
    length = len(element)
    general_length += length

avg_length= general_length / len(sentence_word)
print(avg_length)

