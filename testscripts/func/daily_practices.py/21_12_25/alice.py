def read_file(filename):
    file = open(filename, mode='r', encoding='utf-8')
    text = file.read()
    file.close()
    return text

def clean_text(text):
    text = text.lower()
    clean = ""
    for char in text:
        if char.isalpha():
            clean += char
        else:
            clean += " "
    words = clean.split()
    return words

def word_count(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

max_word = ""
max_count = 0

    for word, freq in count():
      if freq > max_count:
        max_count = freq
        max_word = word
    return max_word, max_count


# text = read_file('alice.txt')
# words = clean_text(text)
# print(words)