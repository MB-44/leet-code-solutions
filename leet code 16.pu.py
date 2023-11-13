def mergeAlternately(word1:str,word2:str):
    list1 = []
    if len(word1) == len(word2):
        k=j=0
        for i in (0,(len(word1)*2)):
            if i%2==1:
                list1.insert(i,word2[j])
                j+=1
            else:
                list1.insert(i,word1[k])
                k+=1
    return list1

test = mergeAlternately("abc","pqr")
print(test)