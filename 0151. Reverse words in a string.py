# 151. Reverse Words in a string
# Medium 
# Two Pointers | String

# Runtime - 4ms

def reverseWords(s):
    s = s.split()
    reversedList = []
    for word in s[::-1]:
        reversedList.append(word.strip())
    return " ".join(reversedList)

s = "the sky is blue"
print(reverseWords(s))