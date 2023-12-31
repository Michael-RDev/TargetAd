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

def load_ad(input_age:str, age_val:list, images:list, gender:str, gen_val:list):
    age = input_age.split("(")[1]
    age = age.split("-")[0]
    age_val = [num.split("-")[0] for num in age_val]

    if age in age_val and gender in gen_val:
        age_indices = [i for i, value in enumerate(age_val) if value == age]
        gender_indices = [i for i, value in enumerate(gen_val) if value == gender]
        common_indeces = list(set(age_indices) & set(gender_indices))
        if common_indeces:
            index = np.random.choice(common_indeces)
            img_path = images[index]
            print(f"Age: {age}")
            print(f"Gender: {gender}")
            print(f"Selected image path: {img_path}")
            img = cv2.imread(img_path)
            img = cv2.resize(img, (1000, 1000))
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
            cv2.moveWindow("Recommended AD", 700, 0)
            cv2.imshow("Recommended AD", img)
            cv2.moveWindow("Recommended AD", 700, 0)
            return img_path

        else:
            print("No matching images found for the given age and gender.")
    else:
        print("Age or gender not found in the provided lists.")
