import mediapipe as mp
import cv2 
import os
import time
import pandas as pd

def draw_landmasks(frame, landmarks, mp_hands):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

def writeToCSV(data_path:str, gender_input:str, age_input:str, store_input:str, is_relevant:bool):
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        df = pd.DataFrame(columns=['age', 'gender', 'store', 'relevant'])

    new_data = {'age': [age_input], 'gender': [gender_input], 'store': [store_input], "relevant": [is_relevant]}  
    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("./data/ad_data.csv", index=False)


def detect_thumb_gesture(camera_object, gender_in:str, age_in:str, store_in:str):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    start_time = time.time()
    close_time = time.time()

    data_feedback = "data/ad_data.csv"

    while True:
        succ, frame = camera_object.read()
        if not succ:
            print("no camera frame thing")
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        thresh = 5

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                thumb_landmark = landmarks.landmark[4]

                thumb_tip_y = thumb_landmark.y
                thumb_is_up = thumb_tip_y < 0.5
                thumb_is_down = thumb_tip_y > 0.6

                end_time = time.time() - start_time
                if end_time > thresh:
                    start_time = time.time()
                    if thumb_is_up:
                        writeToCSV(data_feedback, gender_in, age_in, store_in, True)
                        print("Thumb is up")
                        pass
                    elif thumb_is_down:
                        writeToCSV(data_feedback, gender_in, age_in, store_in, False)
                        print("Thumb is down")
                        pass
                draw_landmasks(frame_rgb, landmarks, mp_hands)
                    
        frame_rgb = cv2.resize(frame_rgb, (1000, 1000))
        cv2.flip(frame_rgb, flipCode=-1)
        cv2.putText(frame_rgb, "Did you find this ad relevant?", (100, 100), 5, 2, (255, 0, 0), 2, 3)
        cv2.putText(frame_rgb,"(Thumbs up or Thumbs down)", (100, 200), 5,2,(255, 0 , 0), 2, 3)
        cv2.imshow("Survey Thing",cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB))
        cv2.moveWindow("Survey Thing", 100, 200)

        check_time =  time.time() - close_time
        if check_time > 10:
            print("Closed da survey")
            break
        if cv2.waitKey(1) == ord('q'):
            break


