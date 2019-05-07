#!/usr/bin/env python

# Bibliotecas necessarias
import rospy
import cv2
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Int32
from sensor_msgs.msg import Image


# Funcao q ira publicar os comandos no topico
def talker():
    # Objeto q ira publicar no topico teleop_topic
    pub = rospy.Publisher('camera_topic', Image, queue_size=10)
    
    # Inicio do node teleop_pub
    rospy.init_node('camera_pub', anonymous=True)

    # Setup da camera 
    cap = cv2.VideoCapture(0)

    while not rospy.is_shutdown():           
        # Captura de um frame na camera
        ret, frame = cap.read()
    
        # Publicacao da img no topico
        rospy.loginfo(frame)    
        pub.publish(frame)

        # Esperar algum tempo para a proxima publicacao
        #time.sleep(2)


# Funcao main
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
