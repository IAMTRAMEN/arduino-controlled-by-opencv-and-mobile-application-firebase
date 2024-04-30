#hedha mghyr connexion maa larduino
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector 
import serial


cap = cv2.VideoCapture(0) 
detector = HandDetector(maxHands=1) 
while True:
        success,img = cap.read() 
        hands,img = detector.findHands(img) 
        if hands: 
            hand = hands[0] 
            fingers= detector.fingersUp(hand) 
            if all(finger == 1 for finger in fingers):
                 x = 1
                 
            else :
                 x=0
            print(fingers[0]) 
        cv2.imshow("OUT",img) 
        if cv2.waitKey(1) == ord('q'): 
            break; 

