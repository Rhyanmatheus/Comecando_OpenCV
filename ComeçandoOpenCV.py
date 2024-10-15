from tabnanny import check

import cv2

video = cv2.VideoCapture('runners.mp4')

while True:
    check,img = video.read()
    cv2.imshow('video',img)
    cv2.waitKey(1)







#img = cv2.imread('farol.jpg')
#imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#print(img.shape)
#cv2.imshow('imagem', img)
#cv2.imshow('imagem CINZA', imgCinza)
#cv2.waitKey(0)

