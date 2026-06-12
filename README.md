# 🤖 Projeto OBR Artística - Detector de Cores com WS2811

## 📌 Descrição

Este projeto foi desenvolvido para a OBR Artística e utiliza Visão Computacional para detectar cores através de uma webcam e controlar uma fita LED WS2811 utilizando um Arduino Uno.

O sistema identifica objetos coloridos em tempo real e altera a cor da fita LED de acordo com a cor detectada.

---

# 🎯 Objetivos

- Detectar cores utilizando OpenCV.
- Processar imagens em tempo real.
- Comunicar Python e Arduino através da Serial USB.
- Controlar uma fita LED WS2811.
- Criar uma interação visual para apresentação na OBR.

---

# 🎨 Mapeamento de Cores

| Cor Detectada | Cor da Fita |
|--------------|-------------|
| 🔵 Azul | 🔵 Azul |
| 🔴 Vermelho | 🟣 Roxo |
| 🟢 Verde | 🟡 Amarelo |
| 🟡 Amarelo | 🟠 Laranja |

---

# 🛠 Materiais Utilizados

## Hardware

- Arduino Uno
- Fita LED WS2811 12V
- Fonte de alimentação 12V
- Webcam
- Notebook
- Cabos Jumper

## Software

- Python 3.x
- Arduino IDE
- OpenCV
- NumPy
- PySerial
- FastLED

---

# 📦 Instalação do Python

Baixe o Python:

https://www.python.org/downloads/

Durante a instalação marque:

```text
Add Python to PATH
```

Verifique a instalação:

```bash
python --version
```

ou

```bash
py --version
```

---

# 📦 Instalação das Bibliotecas

```bash
pip install opencv-python
pip install numpy
pip install pyserial
pip install pygame
```

---

# 📚 Biblioteca Arduino

Instalar pela Arduino IDE:

```text
FastLED
```

---

# 🔌 Ligações

## Arduino → Fita LED

| Arduino | WS2811 |
|----------|---------|
| D6 | DIN |
| GND | GND |

---

## Fonte 12V → Fita LED

| Fonte | WS2811 |
|--------|---------|
| +12V | 12V |
| GND | GND |

---

## Ligação Obrigatória

```text
Fonte GND
     │
     ├── Fita GND
     │
     └── Arduino GND
```

Todos os GNDs devem estar conectados.

---

# 🧠 Funcionamento

```text
Webcam
   ↓
Python (OpenCV)
   ↓
Serial USB
   ↓
Arduino Uno
   ↓
WS2811
```

---

# 🎨 Calibração da Fita

Após testes foi identificado que a ordem correta dos LEDs é:

```cpp
GBR
```

Portanto:

```cpp
FastLED.addLeds<WS2811, LED_PIN, GBR>(leds, NUM_LEDS);
```

---

# 🌈 Cores Utilizadas

## Azul

```cpp
CRGB(0,255,0)
```

## Roxo Escuro

```cpp
CRGB(0,180,180)
```

## Amarelo

```cpp
CRGB(255,0,255)
```

## Laranja

```cpp
CRGB(120,0,255)
```

---

# 🐍 Código Python

Responsável por:

- Captura da webcam
- Processamento da imagem
- Reconhecimento de cores
- Comunicação com Arduino

Bibliotecas utilizadas:

```python
opencv-python
numpy
pyserial
```

---

# 🤖 Código Arduino

Responsável por:

- Receber comandos via Serial
- Interpretar a cor recebida
- Alterar a cor da fita LED

Biblioteca:

```cpp
FastLED
```

---

# 🚀 Fluxo do Projeto

```text
Objeto Azul
     ↓
Webcam
     ↓
Python detecta cor
     ↓
Envia comando serial
     ↓
Arduino recebe
     ↓
Fita LED muda de cor
```

---

# 🔍 Melhorias Futuras

- Reprodução de áudio
- Reconhecimento de personagens
- Interface gráfica
- Integração com IA
- Reconhecimento de voz
- Controle de múltiplas fitas LED

---

# 🏆 Tecnologias Utilizadas

- Python
- OpenCV
- NumPy
- Arduino
- C++
- FastLED
- Comunicação Serial
- Visão Computacional

---

# 👩‍💻 Autoria

Projeto desenvolvido para participação na **OBR Artística**, utilizando Visão Computacional, Arduino e LEDs endereçáveis para criar uma experiência visual interativa baseada em reconhecimento de cores em tempo real.
