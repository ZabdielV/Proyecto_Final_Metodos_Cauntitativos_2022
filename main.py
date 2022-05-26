"""
Emiliano Javier Gómez Jiménez A01377235
Luis Jonathan Rosas Ramos A01377942
Zabdiel Valentin Garduño Vivanco A01377950
"""

import random
import plotly.express as px
import pandas as pd


ejeX = []
ejeY = []
# TCP Method


def TCP():

    # tiempo simulado que transcurre
    tiempo = 0

    # Valor inicial de cwnd
    initialCwnd = 2

    # ritmo en el que se envia paquetes, conocido como Congestion window
    cwnd = initialCwnd

    # limite de velocidad, concido como initial-slow-start-threshold
    sst = 100

    # Variables para simular si hay una perdida o TimeOut

    # connection phase
    print("Sending SYN message")
    print("receiving SYN+ACK message")
    print("starting InitiateTransferPhase")

    # slow start: se incrementa la velocidad de forma exponencial hasta llegar a un limite sst
    while(cwnd < sst):
        cwnd += 1
        tiempo += 0.5
        print("tiempo (s): ", tiempo)
        print("increasing cwnd: ", cwnd)

    print("cwnd is greater than sst, starting Transfer phase")

    # Transfer phase - Congestion Avoidance

    # Se incrementa de forma lineal cwnd hasta que se reporte una perdida (loss) o timeout
    while(tiempo < 100):
        print("Se recibio un ACK, incrementando cwnd")
        if(cwnd >= sst):
            cwnd += 1 / cwnd
        else:
            cwnd += 1

        # simular que hay una perdida
        if(tiempo == 60):
            print("Loss detected ***************")
            cwnd = cwnd/2
            sst = cwnd

        # simular que hay un timeout
        # simular un TimeOut
        if(tiempo == 80):
            print("timeout ************")
            sst = cwnd/2
            cwnd = initialCwnd

        print("cwnd: ", cwnd)
        print("sst: ", sst)
        print("tiempo (s): ", tiempo)
        tiempo += 0.5


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
    print("Sending SYN message")
    print("receiving SYN+ACK message")
    print("starting InitiateTransferPhase")

    # slow start: se incrementa la velocidad de forma exponencial hasta llegar a un limite lws
    while(cwnd < lws):
        cwnd += 1
        tiempo += 0.5
        print("tiempo (s): ", tiempo)
        print("increasing cwnd: ", cwnd)
        ejeX.append(tiempo)
        ejeY.append(cwnd)
    print("cwnd is greater than lws,starting ScalableTCPcongestionAvoidance")

    # Transfer phase - ScalableTCPcongestionAvoidance

    # Se cwnd hasta que se reporte una perdida (loss) o timeout
    while(tiempo < 100):

        print("Se recibio un ACK, incrementando cwnd")
        if(cwnd >= lws):
            cwnd += aS
        else:
            cwnd += 1

        # simular que hay una perdida
        if(tiempo == 60):
            print("Loss detected ***************")
            cwnd = cwnd*bS
            sst = cwnd

        # simular que hay un timeout
        # simular un TimeOut
        if(tiempo == 80):
            print("timeout ************")
            cwnd = cwnd * bS
            sst = cwnd
            cwnd = initialCwnd

        print("cwnd: ", cwnd)
        print("sst: ", sst)
        print("tiempo (s): ", tiempo)
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


main()
