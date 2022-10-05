import mediapipe as mp
import cv2



class Hands:

    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=0)
        self.mpDraw = mp.solutions.drawing_utils
 
    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def hand_type(self):
        if self.results.multi_handedness:
            for classification in self.results.multi_handedness:
                x = classification.classification[0].label
                print(x)

    def find_location(self, img, handNo=0, draw=True):

        li = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                li.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 56, 67), cv2.FILLED)
        return li
