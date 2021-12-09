import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('test.png')
img_sum = np.sum(img, axis=2)
std_img = np.std(img)

std_img = np.where(img_sum<310, std_img, 255)
std_img =  np.where(std_img==255, std_img, 0)
std_img =  np.where(std_img<255, std_img, 1)

img2 = cv2.imread('test.png')
plt.imshow(std_img)
#plt.show()
b, g, r = cv2.split(img2)
b = np.where(std_img!=0,b,168)
g = np.where(std_img!=0,g,198)
r = np.where(std_img!=0,r,198)
std_img= cv2.merge([b,g,r])
#cv2.imwrite("std_img.png", std_img.astype(np.uint8))

#std_img = np.where(std_img!=0,std_img,255)
#std_img = cv2.merge([std_img, std_img, std_img])
#std_img = np.where(std_img!=255,img2,255)
cv2.imwrite('gg.png',std_img)
std_img = cv2.cvtColor(std_img, cv2.COLOR_BGR2RGB)
plt.imshow(std_img)
#cv2.imwrite('gg.png',std_img)
plt.show()