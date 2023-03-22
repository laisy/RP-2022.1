from PIL import Image
import numpy as np

img = Image.open(r'C:\Users\David\Desktop\RP-2022.1\semana 10\imagens\Celula.png')
maxi = np.amax(np.array(img))

for gama in np.arange(1,3.0,0.5):
    im = np.array(img)
    c = (maxi)**(1-gama)
    for i in range(len(im)):
        for k in range(len(im[i])):
            im[i][k] = c*(im[i][k]**gama)
    im = Image.fromarray(im)
    im.save("ResultadoCelula_"+str(gama)+".png")