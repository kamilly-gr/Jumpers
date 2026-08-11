import serial.tools.list_ports

portas = serial.tools.list_ports.comports()

for porta in portas:
    print(porta.device, "-", porta.description)