def count_word_occurrences(sentence):
    word_counts = {}
    words = sentence.lower().split()
    for word in words:
        cleaned_word = word.strip('.,!?;:"\'()[]{}')
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts
text = input("Please enter the sentence: ")
result = count_word_occurrences(text)
print(result)
