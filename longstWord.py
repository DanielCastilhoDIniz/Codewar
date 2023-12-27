"""
#Detail

Countdown is a British game show with number and word puzzles. The letters round consists of the contestant picking 9 shuffled letters - either picking from the vowel pile or the consonant pile. The contestants are given 30 seconds to try to come up with the longest English word they can think of with the available letters - letters can not be used more than once unless there is another of the same character.

#Task

Given an uppercase 9 letter string, letters, find the longest word that can be made with some or all of the letters. The preloaded array words (or $words in Ruby) contains a bunch of uppercase words that you will have to loop through. Only return the longest word; if there is more than one, return the words of the same lengths in alphabetical order. If there are no words that can be made from the letters given, return None/nil/null.

##Examples

letters = "ZZZZZZZZZ"
longest word = None

letters = "POVMERKIA", 
longest word = ["VAMPIRE"]

letters = "DVAVPALEM"
longest word = ["VAMPED", "VALVED", "PALMED"]
"""
# ('TDWAYZROE', ['TODAY', 'TOWER', 'TRADE', 'WATER'])


letters = "TDWAYZROE"
words = ['TOWER', 'TODAY',  'TRADE', 'WATER', 'WAR']


def longest_word(letters):
    return [word for word in words if len(word) == len(max(words, key=len)) and all(letter in letters and word.count(letter) <= letters.count(letter) for letter in set(letters))]


def longest_word1(letters):
    return [word for word in words if len(word) == len(max(words, key=len)) and all(letter in letters for letter in word)]


print(longest_word(letters))
print(longest_word1(letters))


def longest_word2(letters):
    unscrambled = []
    for word in words:
        if set(word).issubset(set(letters)) and all(word.count(l) <= letters.count(l) for l in set(letters)):
            unscrambled.append(word)
    return [x for x in unscrambled if len(x) == max(map(len, unscrambled))] or None


print(longest_word2(letters))


def longest_word3(l):
    c = []
    for i in sorted(words,key=len)[::-1]:
        if all(l.count(j)>=i.count(j) for j in i):
            c+=[i]
    if not c:
        return None
    m = len(c[0])
    return sorted([i for i in c if len(i)==m])

print(longest_word3(letters))