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
lensum = 0
for d in data:
    lensum += len(d)
print('均長',lensum/len(data))

data1=[]
for d in data:
    if len(d)<150:
        data1.append(d)
print('小於150',len(data1))

suck=[]
for d in data:
    if 'suck' in d :
        suck.append(d)
print(suck[0])
print('suck',len(suck))

crap=[]
for d in data:
    if 'crap' in d :
        crap.append(d)
print(crap[0])
print('crap',len(crap))

#jesus=[]
#for d in data:
#    if 'jesus' in d :
#        jesus.append(d)
jesus=[]
jesus = [d for d in data if 'shit' in d]
print(jesus[0])
print('jesus',len(jesus))

爛=[]
爛 = [d for d in data if '爛' in d]
print(爛[0])
print('爛',len(jesus))
