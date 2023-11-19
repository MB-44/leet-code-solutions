# Runtime - 25ms
# Memory = 13.44MB


def isAcronym(words,s):
    firstLetters = ""
    for word in words:
        firstLetters += word[0]
    if firstLetters == s:
        return True
    return False

