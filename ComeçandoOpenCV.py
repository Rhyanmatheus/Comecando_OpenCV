import cv2

img = cv2.imread('farol.jpg')
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#print(img.shape)
cv2.imshow('imagem', img)
cv2.imshow('imagem CINZA', imgCinza)
cv2.waitKey(0)