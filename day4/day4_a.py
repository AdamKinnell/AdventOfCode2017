def is_valid(phrase):
    words = phrase.split()
    return len(set(words)) == len(words)

passphrases = open("day4.txt").readlines()
valid_phrases = list(filter(is_valid, passphrases))
print(len(passphrases), len(valid_phrases))
