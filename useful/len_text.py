# def len_words(text):
#     count_symbols = len(text)
#     count_word = 1
#     count_sentences = 0
#     text = list(text)
#     for i in text:
#         if i == ' ':
#             count_word += 1
#         elif i == '.':
#             count_sentences += 1
#     return count_symbols, count_word, count_sentences
# text = input()
# print(len_words(text))



print("Введите текст:")
text = input()

count_symbols = len(text)

count_word = 0
count_sentences = 0
text = list(text)
for i in text:
    if i == ' ':
        count_word += 1
    elif i == '.':
        count_sentences += 1

print('Символов:', count_symbols)
print('Слов:', count_word + 1)
print('Предложений:', count_sentences)