# https://leetcode.com/problems/ransom-note/description/

def canconstruct(ransomnote, magazine):
    ransom_freq = {}
    magazine_freq = {}

    for char in ransomnote:
        if char in ransom_freq:
            ransom_freq[char] += 1
        else:
            ransom_freq[char] = 1

    for char in magazine:
        if char in magazine_freq:
            magazine_freq[char] += 1
        else:
            magazine_freq[char] = 1

    for char in ransom_freq:
        if ransom_freq[char] > magazine_freq.get(char, 0):
            return False

    return True