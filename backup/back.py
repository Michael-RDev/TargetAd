import cv2
from loadFunctions import getImgs, load_ad
from randomTime import load_survey
from improvedVision import face_mesh
import time

face_proto = "/Users/michael/Desktop/TargetAd/models/face_proto.pbtxt"
face_model = "/Users/michael/Desktop/TargetAd/models/face_model.pb"

gen_proto = "/Users/michael/Desktop/TargetAd/models/gender_proto.prototxt"
gen_model = "/Users/michael/Desktop/TargetAd/models/gender_model.caffemodel"

age_proto = "/Users/michael/Desktop/TargetAd/models/age_proto.prototxt"
age_model = "/Users/michael/Desktop/TargetAd/models/age_model.caffemodel"


face_dnn = cv2.dnn.readNet(face_model, face_proto)
gen_dnn = cv2.dnn.readNet(gen_model, gen_proto)
age_dnn = cv2.dnn.readNet(age_model, age_proto)

gender_groups = ['Male', 'Female']
age_groups = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-41)', '(48-53)', '(60-100)']

FACE_MODEL_MEAN_VALUES = [104, 117, 123]
MODEL_MEAN_VALUES = [78.4263377603, 87.7689143744, 114.895847746]

age = ""

def find_faces(dnn ,dframe, confidence=0.9):
    dnn_frame = dframe.copy()
    frame_height = dnn_frame.shape[0]
    frame_width = dnn_frame.shape[1]

    dnn_blob = cv2.dnn.blobFromImage(dnn_frame, 1.0, (300, 300), [104, 117, 123], True, False)
    dnn.setInput(dnn_blob)
    faces = dnn.forward()

    face_boxes = []

    for i in range(faces.shape[2]):
        dnn_confidence = faces[0,0,i,2]
        if dnn_confidence > confidence:
            x1 = int(faces[0,0,i,3] * frame_width)
            y1 = int(faces[0,0,i,4] * frame_height)

            x2 = int(faces[0,0,i,5] * frame_width)
            y2 = int(faces[0,0,i,6] * frame_height)
            
            face_boxes.append([x1, y1, x2, y2])
            cv2.rectangle(dnn_frame, (x1, y1), (x2, y2), (0, 255, 0), int(round(frame_height / 150)), 8)
    return dnn_frame, face_boxes


img_paths = "/Users/michael/Desktop/TargetAd/imgs"

image, ad_gender, ad_age = getImgs(img_paths)

width = 1000
height = 850
padding = 20



def video_process(cam):
    start_time = time.time()
    while True:
        ready, frame = cam.read()
        if not ready:
            print("no frame found")
            break
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (width, height))

        dnn_frame, face_boxes = find_faces(face_dnn, frame)
        if face_boxes:
            for face_box in face_boxes:
                face = frame[max(0, face_box[1] - padding): 
                            min(face_box[3] + padding, frame.shape[0]- 1), 
                            max(0, face_box[0] - padding): 
                            min(face_box[2] + padding, frame.shape[1] - 1)]
                
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

                gen_dnn.setInput(blob=blob)
                gen_preds = gen_dnn.forward()
                gender = gender_groups[gen_preds[0].argmax()]
                
                age_dnn.setInput(blob=blob)
                age_preds = age_dnn.forward()
                age = age_groups[age_preds[0].argmax()]
            
                thresh = 5

                if age and time.time() - start_time >= thresh:
                    load_ad(input_age=age, age_val=ad_age, images=image)
                    start_time = time.time()
                else:
                    pass
        
                cv2.putText(dnn_frame, f'{gender}, {age}', (face_box[0], face_box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

        load_survey(cam)
        cv2.imshow("age video idk", dnn_frame)
        
        
        if cv2.waitKey(2) == ord('q'):
            break



while __name__ == "__main__":
    cam = cv2.VideoCapture(1)
    #video_process(cam)
    face_mesh(cam)
    cam.release()
    cv2.destroyAllWindows()
