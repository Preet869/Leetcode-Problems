sentence = "Hello World"

def full_reverse(sentence):
    words = sentence.split()
    reversed_words = []

    for i in range(len(words) -1, -1, -1):
        reversed_word = words[i][::-1]
        reversed_words.append(reversed_word)
    
    return " ".join(reversed_words)

print(full_reverse(sentence))