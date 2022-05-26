"""
Emiliano Javier Gómez Jiménez A01377235
Luis Jonathan Rosas Ramos A01377942
Zabdiel Valentin Garduño Vivanco A01377950
"""

import plotly.express as px
import pandas as pd
from pathlib import Path

myfile = Path('./pruebas.txt')
myfile.touch(exist_ok=True)
f = open('pruebas.txt', 'r+')

ejeX = []
ejeY = []

def scalableTCP():

    # tiempo simulado que transcurre
    tiempo = 0

    # Valor inicial de cwnd
    initialCwnd = 2

    # ritmo en el que se envia paquetes, conocido como Congestion window
    cwnd = initialCwnd

    # limite de velocidad, concido como initial-slow-start-threshold
    sst = 100

    # Variables para simular si hay una perdida o TimeOut

    lws = 16
    aS = 0.01
    bS = 0.875

    # connection phase
    f.write("Sending SYN message\n")
    f.write("Receiving SYN+ACK message\n")
    f.write("Starting InitiateTransferPhase\n")
    f.write("--------------------------------------\n")

    # slow start: se incrementa la velocidad de forma exponencial hasta llegar a un limite lws
    while(cwnd < lws):
        cwnd += 1
        tiempo += 0.5
        f.write("tiempo (s): " + str(tiempo) + "\n")
        f.write("increasing cwnd: " + str(cwnd) + "\n")
        ejeX.append(tiempo)
        ejeY.append(cwnd)
    f.write("cwnd is greater than lws,starting ScalableTCPcongestionAvoidance\n")

    # Transfer phase - ScalableTCPcongestionAvoidance

    # Se cwnd hasta que se reporte una perdida (loss) o timeout
    while(tiempo < 100):

        f.write("Se recibio un ACK, incrementando cwnd\n")
        if(cwnd >= lws):
            cwnd += aS
        else:
            cwnd += 1

        # simular que hay una perdida
        if(tiempo == 60):
            f.write("Loss detected ***************\n")
            cwnd = cwnd*bS
            sst = cwnd

        # simular que hay un timeout
        # simular un TimeOut
        if(tiempo == 80):
            f.write("Timeout ************\n")
            cwnd = cwnd * bS
            sst = cwnd
            cwnd = initialCwnd

        f.write("cwnd: " + str(cwnd) + "\n")
        f.write("sst: " + str(sst) + "\n")
        f.write("tiempo (s): " + str(tiempo) + "\n")
        tiempo += 0.5
        ejeX.append(tiempo)
        ejeY.append(cwnd)


def main():

    # TCP()
    scalableTCP()
    df = pd.DataFrame(dict(
        tiempoEnSegundos=ejeX,
        cwnd=ejeY
    ))

    fig = px.line(df, x='tiempoEnSegundos', y="cwnd",
                  title="Scalable TCP Congestion Avoidance (simulación)")

    fig.show()
    f.write('-------------------------------------\n')
    f.close()


main()
