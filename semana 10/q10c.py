from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\David\Desktop\RP-2022.1\semana 10\imagens\GorisRaioni.jpg')
maxi = np.amax(np.array(img))

for gama in np.arange(4,7,0.5):
    im = np.array(img)
    c = (maxi)**(1-gama)
    for i in range(len(im)):
        for k in range(len(im[i])):
            im[i][k] = c*(im[i][k]**gama)
    im = Image.fromarray(im)
    im.save("Resultado_"+str(gama)+".png")