import os


train = open('ImageSets/Main/train_test.txt','w')
train.truncate()

test = open('ImageSets/Main/test.txt','w')


datasets = [f for f in os.listdir('JPEGImages/') if f.endswith('.jpg')]
print(len(datasets))
count = 0
for s in datasets:
       s = s.replace('.jpg','')
       if count < len(datasets)/8*5:
              train.write(s +'\n')
       else:
              test.write(s + '\n')
       count= count + 1

#print(datasets)