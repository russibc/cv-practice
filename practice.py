# pip install numpy
# pip install opencv-python
import cv2 as c

print("Abrindo imagem...")
imagenRGB = c.imread('practice.jpg')

b, g, r = c.split(imagenRGB)

c.imshow('Canal Roxo', r)
c.imshow('Canal Verde', g)
c.imshow('Canal Azul', b)

c.imwrite('canal_roxo.jpg', r)
c.imwrite('canal_verde.jpg', g)
c.imwrite('canal_azul.jpg', b)

c.waitKey(0)
c.destroyAllWindows()
