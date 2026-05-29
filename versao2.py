import cv2
import numpy as np
import serial
import time

# 🔌 ajuste a porta COM
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

ultima_cor = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 🎨 máscaras de cor
    azul = cv2.inRange(hsv, (100, 150, 0), (140, 255, 255))
    amarelo = cv2.inRange(hsv, (20, 100, 100), (35, 255, 255))
    laranja = cv2.inRange(hsv, (10, 100, 100), (20, 255, 255))
    vermelho = cv2.inRange(hsv, (0, 120, 70), (10, 255, 255))

    cor = None

    if cv2.countNonZero(azul) > 5000:
        cor = "AZUL"

    elif cv2.countNonZero(vermelho) > 5000:
        cor = "ROXO"   # mapeado depois no Arduino

    elif cv2.countNonZero(amarelo) > 5000:
        cor = "AMARELO"

    elif cv2.countNonZero(laranja) > 5000:
        cor = "LARANJA"

    # 🚀 envia só se mudar a cor
    if cor and cor != ultima_cor:
        arduino.write((cor + "\n").encode())
        ultima_cor = cor

    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()