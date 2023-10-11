import numpy as np
from showSurvey import detect_thumb_gesture
import cv2

def load_survey(camera_obj, gender_in:str, age_in:str, store_in:str):
    randNum = np.random.randint(0, 500)
    if randNum < 250:
        detect_thumb_gesture(camera_obj, gender_in, age_in, store_in)
        camera_obj.release()
        cv2.destroyAllWindows()
