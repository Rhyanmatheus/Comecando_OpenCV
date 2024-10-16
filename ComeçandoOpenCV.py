from tabnanny import check

import cv2

camera = cv2.VideoCapture(0)
camera.set(3,640) #largura
camera.set(4,420) #altura
camera.set(10,100) # Brilho/luminosidade

while True:
    check,img = camera.read()
    cv2.imshow('webcam',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break










#video = cv2.VideoCapture('runners.mp4')

#while True:
    #check,img = video.read()
    #imgRedim = cv2.resize(img,(640,420))
    #cv2.imshow('video',imgRedim)
    #cv2.waitKey(10)







#img = cv2.imread('farol.jpg')
#imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#print(img.shape)
#cv2.imshow('imagem', img)
#cv2.imshow('imagem CINZA', imgCinza)
#cv2.waitKey(0)

