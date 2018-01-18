def is_valid(phrase):
    words = phrase.split()
    return len(set(words)) == len(words)

passphrases = open("day4.txt").readlines()
valid_phrases = list(filter(is_valid, passphrases))

print('Valid Passphrases:', len(valid_phrases)) # = 337
