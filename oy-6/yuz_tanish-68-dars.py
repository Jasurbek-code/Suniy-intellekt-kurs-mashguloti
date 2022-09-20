import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cvlib as cv

model = load_model('glass.model')  # modelni uqitish uchun fayl nomi     ## .model --> quyilishi kerak
turi = ['Glass', 'Without_Glass']  # rasmlar joylashgan fayl nomi

video = cv2.VedioCapture('1.mp4')  # modelni uqitganda shu faylni ochib beradi,  0 (nol) quyilsa kamerani ochib beradi

while video.isOpened():
    boolean, kadr = video.read()
    face, confindence = cv.detect_face(kadr)

    for index, yuz in enumerate(face):
        (startX, startY, endX, endY) = yuz[1], yuz[2], yuz[3], yuz[4]

        yuz_np = np.copy(kadr[startY:endY, startX:endX])

        if (yuz_np.shape[0] < 10) or (yuz_np.shape[1] < 10):
            continue

        yuz_np = cv2.resize(yuz_np, (96, 96))
        yuz_np = yuz_np.astype('float') / 255.0
        yuz.np = img_to_array(yuz_np)
        yuz_np = np.expand_dims(yuz_np, axis=0)

        bashorat = model.predict(yuz_np)[0]

        index = np.argmax(bashorat)
        label = turi[index]

        if label == 'Glass':
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        label = f"{label} {np.around(bashorat[index] * 100, 2)}"

        cv2.putText(kadr, label, (startX, startY), (endX, endY), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.rectangle(kadr, (startY, startY), (endX, endY), color, 2)

    cv2.imshow('AI darsimiz', kadr)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # tugma bosmagunimizcha oyna yopilmaydi
        break

video.release()
cv2.destroyAllWindows()




