import os
import cv2
from multiprocessing import Process, Queue, Value, Lock

import face_recognition


def predict_face():
    pass

def draw_face():
    pass

def get_face():
    pass

def show():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow('Face Gender Classification', frame)

            key = cv2.waitKey(25)    
            if key == ord('q'):
                break
        else:
            print("Can not caputre from this camera!")
            break
    
    cv2.destroyAllWindows()

def main():
    input_queue  = Queue(maxsize=1024)
    face_queue   = Queue(maxsize=1024)
    output_queue = Queue(maxsize=1024)
    
    show()



if __name__=='__main__':
    main()
