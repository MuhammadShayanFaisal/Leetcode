def firstUniqChar(s):
    List=list("".join(dict.fromkeys(s)))
    if (len(s)<2):
        return 0
    for i in List:
        if s.count(i)==1:
            return s.find(i)
        continue
    return -1
print(firstUniqChar('loveleetcode'))