import  sys
num = int(sys.stdin.readline())

chracterList =[]
for i in range(num):
    charcter = sys.stdin.readline().strip("\n")
    wordlen = len(charcter)
    chracterList.append((wordlen,charcter))

chracterList = list(set(chracterList))
chracterList.sort(key=lambda word: (word[0], word[1]))
for j in chracterList:
    print(j[1])