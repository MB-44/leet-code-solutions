def isSubsequence(s:str,t:str):
    for letter in s:
        if letter in t:
            t.replace(letter,"",1)
        else: 
            return False
    return True
