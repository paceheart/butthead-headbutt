with open('/usr/share/dict/words', 'r') as wordsFile:
    wordsList = [line.strip() for line in wordsFile.readlines()]
wordsSet = set(wordsList)
for headbutt in wordsList:
    if headbutt.isalpha() and headbutt.islower():
        length = len(headbutt)
        if length >= 6:
            for i in range(length - 5): # only consider words of length 3 or more
                head = headbutt[0:i+3]
                butt = headbutt[i+3:]
                butthead = butt + head
                if head < butt and head in wordsSet and butt in wordsSet and butthead in wordsSet and headbutt != butthead:
                    print(headbutt + " / " + butthead)
