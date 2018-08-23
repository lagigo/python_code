data = []
count = 0

import progressbar
bar = progressbar.ProgressBar(max_value=1000000)


with open ('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
#        if count % 1000==0:
#        print(len(data))
print('讀完,有',len(data),'留言')

worddict = {}
for d in data:
    words = d.split (' ')
    for word in words:
        count += 1
        if count % 100000 == 0:
            print(count)
            print(len(worddict))
        if word in worddict :
            worddict[word] += 1
        else :
            worddict[word] = 1

for word in worddict:
    if worddict[word]>1000:
        print (word,worddict[word])
print (len)

while True:
    word = input ('查甚麼:')
    if word == 'q':
        print ('exit')
        break
    if word in worddict:
        print (word,'次數',worddict[word])
    else :
        print('沒這個字')





