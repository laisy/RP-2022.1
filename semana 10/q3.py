import cv2
import numpy as np


im=cv2.imread(r'C:\Users\David\Desktop\RP-2022.1\semana 10\imagens\Fig0308(a)(fractured_spine).png', cv2.IMREAD_GRAYSCALE) / 255
res = np.full((im.shape[0],im.shape[1]),0,np.uint8)
maxi = 255

# for i in range(len(im)):
#     c = (maxi)/np.log(maxi+1)
#     for k in range(len(im[i])):
#         im[i][k] = c*np.log(1+im[i][k])
# im = Image.fromarray(im)
# im.save('resultado.png')

for gama in np.arange(0.4,0.7,0.1):
    c = (maxi)/np.log10(maxi+1)
    print(c)
    for i in range(len(res)):
        for k in range(len(res[i])):
            res[i][k] = c*np.log10(1+res[i][k])
            print(res[i][k])
    cv2.imwrite("Resultado_"+str(gama)+".png",res)
    res = np.full((im.shape[0],im.shape[1]),0,np.uint8)