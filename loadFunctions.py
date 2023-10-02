import os
import cv2
import numpy as np

def getImgs(input_path:str):
    images = []
    age = []
    gen = []
    for age_group in os.listdir(input_path):
        full_age_path = os.path.join(input_path, age_group)
        for folder in os.listdir(full_age_path):
            img_path = os.path.join(full_age_path, folder)
            for gender in os.listdir(img_path):
                gender_paths = os.path.join(img_path, gender)
                images.append(gender_paths)
                age.append(img_path.split("/")[-2])
                gen.append(img_path.split("/")[-1])
    return images, gen, age    


def load_ad(input_age:str, age_val:list, images:list):
    indexs = []
    age = input_age.split("(")[1]
    age = age.split("-")[0]
    age_val = [num.split("-")[0] for num in age_val]
    if age in age_val:
        indexs = [returnIndx for returnIndx, value in enumerate(age_val) if value == age]
        randIndx = np.random.randint(len(indexs))
        index = indexs[randIndx]
        img_path = images[index]
        img = cv2.imread(img_path)
        img = cv2.resize(img, (700, 700))
        img = img / 255.0
        img_path_updated = img_path.split("/")[-1]
        img_path_updated = img_path_updated.split(".")[0]
        font_scale = min(img.shape[0], img.shape[1]) / 1000.0
        font_size = int(1.5 * font_scale)
        text_position = (100, 100)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 255, 0)
        thickness = 2
        cv2.putText(img, f"Available Products: {img_path_updated}", text_position, font, font_size, color, thickness, cv2.LINE_AA)
        cv2.moveWindow("ad ting", 700, 0)
        cv2.imshow("ad ting", img)
        return img_path
