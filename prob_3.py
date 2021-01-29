infile = open("word.txt",'r')
d = dict()

for line in infile:
    line = line.strip()
    # print(line)
    words = line.split(" ")
    # print(words)
    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1

print ("\n The total numbers in file are : ", d)

for key in list(d.keys()):
    str1 = key+":"+ str(d[key])
    # print(str1)
    text1 = open("word.txt", "a")
    text1.write('\n')
    text1.write(str1)
