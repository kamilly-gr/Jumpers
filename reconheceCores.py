import cv2
import numpy as np

cap = cv2.VideoCapture(1)

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
        ("VERMELHO", vermelho, (0, 0, 255)),
        ("AMARELO", amarelo, (0, 255, 255)),
        ("LARANJA", laranja, (0, 165, 255))
    ]

    for nome, mascara, cor_bgr in cores:

        contornos, _ = cv2.findContours(
            mascara,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contorno in contornos:

            area = cv2.contourArea(contorno)

            if area > 90000:

                x, y, w, h = cv2.boundingRect(contorno)

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

    cv2.imshow("Teste Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()