def sort_and_count_duplicates(inputlist):
    counts = {}
    for num in inputlist:
        counts[num] = counts.get(num, 0) + 1
    
    sortedlist = sorted(inputlist, key=lambda x: (counts[x], x))
    return sortedlist

inputlist = [1,2,3,4,1,2,3,1,1,1,1,1]
output = sort_and_count_duplicates(inputlist)
print(output)