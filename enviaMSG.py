import cv2
import numpy as np
import serial
import time

# Ajuste a porta se necessário
arduino = serial.Serial('COM5', 9600)

# Espera o Arduino reiniciar
time.sleep(4)

cap = cv2.VideoCapture(1)

ultima_cor = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Azul
    blue_mask = cv2.inRange(
        hsv,
        np.array([100,150,0]),
        np.array([140,255,255])
    )

    # Vermelho
    red1 = cv2.inRange(
        hsv,
        np.array([0,120,70]),
        np.array([10,255,255])
    )

    red2 = cv2.inRange(
        hsv,
        np.array([170,120,70]),
        np.array([180,255,255])
    )

    red_mask = red1 + red2

    # Verde
    green_mask = cv2.inRange(
        hsv,
        np.array([40,70,70]),
        np.array([80,255,255])
    )

    # Amarelo
    yellow_mask = cv2.inRange(
        hsv,
        np.array([20,100,100]),
        np.array([35,255,255])
    )

    cor = None

    if cv2.countNonZero(blue_mask) > 5000:
        cor = "AZUL"

    elif cv2.countNonZero(red_mask) > 5000:
        cor = "ROXO"

    elif cv2.countNonZero(green_mask) > 5000:
        cor = "AMARELO"

    elif cv2.countNonZero(yellow_mask) > 5000:
        cor = "LARANJA"

    if cor:

        cv2.putText(
            frame,
            cor,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        if cor != ultima_cor:

            print("Enviado:", cor)

            arduino.write((cor + "\n").encode())

            ultima_cor = cor

    cv2.imshow("Detector de Cores", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()