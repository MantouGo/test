import os




datasets = [f for f in os.listdir('Annotations/') if f.endswith('.txt')]
print(datasets)

tmp = ""
for s in datasets:
	train = open('C:/Users/riverkidden/Desktop/keras-frcnn-master/keras_frcnn/VOCDevkit2007/VOC2007/Annotations/'+s,'r')
	#tmp = ""
	line = train.readline()
	while line:
		#print(line)
		#line = line.replace('aircraft_','C:/Users/riverkidden/Desktop/keras-frcnn-master/keras_frcnn/VOCDevkit2007/VOC2007/Annotations/JPEGImages/aircraft_')
		#line = line.replace('	',',')
		#line = line.replace(' ',',')
		#line = line.replace(',aircraft','')
		#line = line.replace('\n',',aircraft\n')
		tmp = tmp + line
		line = train.readline()
	#file = file.replace('<?xml version="1.0" encoding="utf-8"?>\n','')
	#train.seek(0)
	train.close()
	#train = open('C:/Users/riverkidden/Desktop/keras-frcnn-master/keras_frcnn/VOCDevkit2007/VOC2007/Annotations/'+s,'w')
	#train.write(tmp)
	#train.close()
	#os.system("pause")
train = open('C:/Users/riverkidden/Desktop/keras-frcnn-master/keras_frcnn/VOCDevkit2007/VOC2007/Annotations/my_data.txt','w')
train.write(tmp)
train.close()