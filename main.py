import os
import cv2
from threading import Thread
from multiprocessing import Queue, Value, Lock

# from utils import face_recognition


def show(result_queue, mp_running):
    """
    Show resultq
    """
    while mp_running.value:
        if not result_queue.empty():
            img = result_queue.get()

            cv2.imshow("Face Gender Classification!", img)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                mp_running.value = 0
                break
    cv2.destroyAllWindows()

def capture(frame_queue, mp_running):
    """
    """
    cam = cv2.VideoCapture(0)
    while mp_running.value:
        ret, frame = cam.read()
        if ret:
            if frame_queue.empty():
                frame_queue.put(frame)


def main():
    input_queue  = Queue(maxsize=1024)
    face_queue   = Queue(maxsize=1024)
    output_queue = Queue(maxsize=1024)
    
    mp_running = Value('i', 1)

    captureThread = Thread(target=capture, args=(input_queue, mp_running), daemon=True)
    captureThread.start()
    showThread = Thread(target=show, args=(input_queue, mp_running), daemon=True)
    showThread.start()
    
    while mp_running.value:
        continue
    
    while not input_queue.empty():
        _ = input_queue.get()

    captureThread.join()
    showThread.join()



if __name__=='__main__':
    main()
