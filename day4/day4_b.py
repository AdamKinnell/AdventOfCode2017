def is_valid(phrase):
    words = phrase.split()
    word_letters = list(map("".join, map(sorted, words)))
    return len(set(word_letters)) == len(words)

passphrases = open("day4.txt").readlines()
valid_phrases = list(filter(is_valid, passphrases))
print(len(passphrases), len(valid_phrases))
