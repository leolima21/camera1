#!/usr/bin/env python

# Bibliotecas necessarias
import rospy
import cv2
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image


# Funcao q ira executar o movimento do robo
def callback(data):
    # Criação do objeto da imagem
    ret, frame = data.data

    # Exibir a imagem em uma janela
    cv2.imshow('frame', frame)

    # Fechar a janela pressionando a tecla 'q'
	if cv2.waitKey(1) == ord('q'):
		break


def listener():
    # Inicio do node camera_sub
    rospy.init_node('camera_sub', anonymous=True)

    # Inscricao no topico e definicao da callback como funcao a ser executada
    rospy.Subscriber("camera_topic", Image, callback)

    # Mantem o python funcionando apos o encerramendo do node
    rospy.spin()


# Funcao main
if __name__ == '__main__':
    listener()