# 🎯 Versão:
# 📷🎨🔊 “Detecção de cores + áudio em tempo real”

# Ela já possui:

# ✅ Webcam em tempo real
# ✅ Conversão para HSV
# ✅ Detecção de 4 cores
# ✅ Controle para não repetir áudio infinitamente
# ✅ Threads para não travar a câmera
# ✅ Nome da cor na tela
# audios salvos nesse formato : vermelho.mp3, azul.mp3, verde.mp3, amarelo.mp3



import cv2
import numpy as np
import pygame
import threading
import time

# 🔊 iniciar áudio
pygame.mixer.init()

ultima_cor = None
tempo_ultimo_audio = 0
cooldown = 2  # segundos entre áudios

# 🎵 função de áudio
def tocar_audio(nome):
    pygame.mixer.music.load(nome)
    pygame.mixer.music.play()

# 📷 webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 🔴 vermelho (duas faixas)
    red1 = cv2.inRange(hsv, np.array([0,120,70]), np.array([10,255,255]))
    red2 = cv2.inRange(hsv, np.array([170,120,70]), np.array([180,255,255]))
    red_mask = red1 + red2

    # 🔵 azul
    blue_mask = cv2.inRange(hsv, np.array([100,150,0]), np.array([140,255,255]))

    # 🟢 verde
    green_mask = cv2.inRange(hsv, np.array([40,70,70]), np.array([80,255,255]))

    # 🟡 amarelo
    yellow_mask = cv2.inRange(hsv, np.array([20,100,100]), np.array([35,255,255]))

    cor_detectada = None

    # 🎯 detectar cor
    if cv2.countNonZero(blue_mask) > 5000:
        cor_detectada = "azul"
    elif cv2.countNonZero(red_mask) > 5000:
        cor_detectada = "vermelho"
    elif cv2.countNonZero(green_mask) > 5000:
        cor_detectada = "verde"
    elif cv2.countNonZero(yellow_mask) > 5000:
        cor_detectada = "amarelo"

    # 🔊 tocar áudio com controle
    if cor_detectada:
        if (cor_detectada != ultima_cor) or (time.time() - tempo_ultimo_audio > cooldown):

            threading.Thread(
                target=tocar_audio,
                args=(f"{cor_detectada}.mp3",)
            ).start()

            ultima_cor = cor_detectada
            tempo_ultimo_audio = time.time()

        # 🖥️ mostrar na tela
        cv2.putText(frame,
                    cor_detectada.upper(),
                    (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2)

    # 📺 mostrar imagem
    cv2.imshow("Detector de Cores", frame)

    # sair com Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()