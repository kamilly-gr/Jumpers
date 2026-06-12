import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

ultima_cor = ""

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Azul
    azul = cv2.inRange(hsv, (100,150,0), (140,255,255))

    # Vermelho
    vermelho1 = cv2.inRange(hsv, (0,120,70), (10,255,255))
    vermelho2 = cv2.inRange(hsv, (170,120,70), (180,255,255))
    vermelho = vermelho1 + vermelho2

    # Verde
    verde = cv2.inRange(hsv, (40,70,70), (80,255,255))

    # Amarelo
    amarelo = cv2.inRange(hsv, (20,100,100), (35,255,255))

    cor = None

    if cv2.countNonZero(azul) > 5000:
        cor = "AZUL"

    elif cv2.countNonZero(vermelho) > 5000:
        cor = "ROXO"

    elif cv2.countNonZero(verde) > 5000:
        cor = "AMARELO"

    elif cv2.countNonZero(amarelo) > 5000:
        cor = "LARANJA"

    if cor and cor != ultima_cor:
        arduino.write((cor + "\n").encode())
        ultima_cor = cor

    cv2.imshow("Detector de Cores", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()