import cv2
import numpy as np
import serial
import time
#Versão mais completa com area limite de detecção de cor, e envio para o arduino
# ======== Arduino ========
arduino = serial.Serial('COM5', 9600)  # Altere se necessário
time.sleep(2)

# ======== Câmera ========
cap = cv2.VideoCapture(1)

ultima_cor = ""

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Máscaras de cores
    azul = cv2.inRange(hsv, (100, 150, 0), (140, 255, 255))

    vermelho1 = cv2.inRange(hsv, (0, 120, 70), (10, 255, 255))
    vermelho2 = cv2.inRange(hsv, (170, 120, 70), (180, 255, 255))
    vermelho = vermelho1 + vermelho2

    amarelo = cv2.inRange(hsv, (20, 100, 100), (35, 255, 255))
    laranja = cv2.inRange(hsv, (10, 100, 100), (20, 255, 255))

    cores = [
        ("AZUL", azul, (255, 0, 0)),
        ("ROXO", vermelho, (255, 0, 255)),     # Vermelho da câmera → Roxo no LED
        ("AMARELO", amarelo, (0, 255, 255)),
        ("LARANJA", laranja, (0, 165, 255))
    ]

    cor_detectada = None

    for nome, mascara, cor_bgr in cores:

        contornos, _ = cv2.findContours(
            mascara,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if contornos:

            maior = max(contornos, key=cv2.contourArea)
            area = cv2.contourArea(maior)

            if area > 90000:

                x, y, w, h = cv2.boundingRect(maior)

                cv2.rectangle(frame, (x, y), (x+w, y+h), cor_bgr, 2)

                cv2.putText(
                    frame,
                    nome,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    cor_bgr,
                    2
                )

                cor_detectada = nome

    # ======== Envia para o Arduino ========
    if cor_detectada and cor_detectada != ultima_cor:

        print("Enviado:", cor_detectada)

        arduino.write((cor_detectada + "\n").encode())

        ultima_cor = cor_detectada

    cv2.imshow("Teste Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()