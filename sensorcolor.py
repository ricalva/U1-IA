from pickletools import uint1, uint8
from tkinter import Frame
import cv2
import numpy as np

#Sensar color mediante la camara 
#Rango y color para sensar

colorin = np.array([115,100,20], np.uint8)
colorfi = np.array([125,255,128], np.uint8)

colorin2 = np.array([175,150,20], np.uint8)
colorfi2 = np.array([180,255,255], np.uint8)

cam = cv2.VideoCapture(0)

while True:
    ban, frameBGR = cam.read()
    #invertir la camara y que no se vea como espejo 
    frameBGR = cv2.flip(frameBGR,1)

    #Converitir imagen de BGR a HSV
    frameHSV = cv2.cvtColor(frameBGR,cv2.COLOR_BGR2HSV)

    #Detectar colores 
    detecta = cv2.inRange(frameHSV, colorin, colorfi)
    detecta2 = cv2.inRange(frameHSV, colorin2, colorfi2)
    mix = cv2.add(detecta, detecta2)

    #Usando Bitwise para ,mostrar las foto gramas

    imagenBitwise = cv2.bitwise_and(frameBGR, frameBGR, mask=mix)

    #Condicion para mostrar la fotograma 
    if ban == True:
        cv2.imshow("Camara On", frameBGR)
        cv2.imshow("Camara HSV", frameHSV)
        cv2.imshow("Camara Detectar", detecta)
        cv2.imshow("Camara Detectar", mix)
        #Condicion para apagar la camara 
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
        

cam.release()
cv2.destroyAllWindows()