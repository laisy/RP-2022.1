import cv2
import numpy as np

def otsu(img):
    ret, res = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return res

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig1039(a)(polymersomes).png', cv2.IMREAD_GRAYSCALE)

imgheight=img.shape[0]
imgwidth=img.shape[1]

y1 = 0
M = imgheight//3
N = imgwidth//3
cnt = 0
temp = []
for y in range(0,imgheight,M):
    for x in range(0, imgwidth, N):
        y1 = y + M
        x1 = x + N
        tile = img[y:y+M,x:x+N]

        # cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0))#grid
        # cv2.imwrite(str(cnt)+".png",tile)
        cnt +=1
        tile = otsu(tile)
        temp.append(tile)
final = []
for i in range(0,9,3):
    resH = np.concatenate((temp[i],temp[i+1],temp[i+2]),axis=1)
    final.append(resH)

resV = np.concatenate((final[0],final[1],final[2]),axis=0)

cv2.imwrite("grid.png",resV)

cv2.imwrite("global.png",otsu(img))